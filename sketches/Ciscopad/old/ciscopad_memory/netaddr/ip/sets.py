def _subtract(supernet, subnets, subnet_idx, ranges):
    version = supernet._module.version
    subnet = subnets[subnet_idx]
    if subnet.first > supernet.first:
        ranges.append((version, supernet.first, subnet.first - 1))

    subnet_idx += 1
    prev_subnet = subnet
    while subnet_idx < len(subnets):
        cur_subnet = subnets[subnet_idx]

        if cur_subnet not in supernet:
            break
        if prev_subnet.last + 1 == cur_subnet.first:
            # two adjacent, non-mergable IPNetworks
            pass
        else:
            ranges.append((version, prev_subnet.last + 1, cur_subnet.first - 1))

        subnet_idx += 1
        prev_subnet = cur_subnet

    first = prev_subnet.last + 1
    last = supernet.last
    if first <= last:
        ranges.append((version, first, last))

    return subnet_idx

def _iter_merged_ranges(sorted_ranges):
    if not sorted_ranges:
        return

    current_version, current_start, current_stop = sorted_ranges[0]

    for next_version, next_start, next_stop in sorted_ranges[1:]:
        if next_start == current_stop + 1 and next_version == current_version:
            # Can be merged.
            current_stop = next_stop
            continue
        # Cannot be merged.
        yield (IPAddress(current_start, current_version),
               IPAddress(current_stop, current_version))
        current_start = next_start
        current_stop = next_stop
        current_version = next_version
    yield (IPAddress(current_start, current_version),
           IPAddress(current_stop, current_version))

class IPSet(object):
    __slots__ = ('_cidrs', '__weakref__')

    def __init__(self, iterable=None, flags=0):
        if isinstance(iterable, IPNetwork):
            self._cidrs = {iterable.cidr: True}
        elif isinstance(iterable, IPRange):
            self._cidrs = dict.fromkeys(
                iprange_to_cidrs(iterable[0], iterable[-1]), True)
        elif isinstance(iterable, IPSet):
            self._cidrs = dict.fromkeys(iterable.iter_cidrs(), True)
        else:
            self._cidrs = {}
            if iterable is not None:
                mergeable = []
                for addr in iterable:
                    if isinstance(addr, _int_type):
                        addr = IPAddress(addr, flags=flags)
                    mergeable.append(addr)

                for cidr in cidr_merge(mergeable):
                    self._cidrs[cidr] = True

    def __getstate__(self):
        return tuple([cidr.__getstate__() for cidr in self._cidrs])

    def __setstate__(self, state):
        self._cidrs = dict.fromkeys(
            (IPNetwork((value, prefixlen), version=version)
             for value, prefixlen, version in state),
            True)

    def _compact_single_network(self, added_network):
        added_first = added_network.first
        added_last = added_network.last
        added_version = added_network.version

        # Check for supernets and subnets of added_network.
        if added_network._prefixlen == added_network._module.width:
            # This is a single IP address, i.e. /32 for IPv4 or /128 for IPv6.
            # It does not have any subnets, so we only need to check for its
            # potential supernets.
            for potential_supernet in added_network.supernet():
                if potential_supernet in self._cidrs:
                    del self._cidrs[added_network]
                    return
        else:
            # IPNetworks from self._cidrs that are subnets of added_network.
            to_remove = []
            for cidr in self._cidrs:
                if (cidr._module.version != added_version or cidr == added_network):
                    # We found added_network or some network of a different version.
                    continue
                first = cidr.first
                last = cidr.last
                if first >= added_first and last <= added_last:
                    # cidr is a subnet of added_network. Remember to remove it.
                    to_remove.append(cidr)
                elif first <= added_first and last >= added_last:
                    # cidr is a supernet of added_network. Remove added_network.
                    del self._cidrs[added_network]
                    # This IPSet was properly compacted before. Since added_network
                    # is removed now, it must again be properly compacted -> done.
                    assert (not to_remove)
                    return
            for item in to_remove:
                del self._cidrs[item]

        # Check if added_network can be merged with another network.

        # Note that merging can only happen between networks of the same
        # prefixlen. This just leaves 2 candidates: The IPNetworks just before
        # and just after the added_network.
        # This can be reduced to 1 candidate: 10.0.0.0/24 and 10.0.1.0/24 can
        # be merged into into 10.0.0.0/23. But 10.0.1.0/24 and 10.0.2.0/24
        # cannot be merged. With only 1 candidate, we might as well make a
        # dictionary lookup.
        shift_width = added_network._module.width - added_network.prefixlen
        while added_network.prefixlen != 0:
            # figure out if the least significant bit of the network part is 0 or 1.
            the_bit = (added_network._value >> shift_width) & 1
            if the_bit:
                candidate = added_network.previous()
            else:
                candidate = added_network.next()

            if candidate not in self._cidrs:
                # The only possible merge does not work -> merge done
                return
            # Remove added_network&candidate, add merged network.
            del self._cidrs[candidate]
            del self._cidrs[added_network]
            added_network.prefixlen -= 1
            # Be sure that we set the host bits to 0 when we move the prefixlen.
            # Otherwise, adding 255.255.255.255/32 will result in a merged
            # 255.255.255.255/24 network, but we want 255.255.255.0/24.
            shift_width += 1
            added_network._value = (added_network._value >> shift_width) << shift_width
            self._cidrs[added_network] = True

    def compact(self):
        cidrs = cidr_merge(self._cidrs)
        self._cidrs = dict.fromkeys(cidrs, True)

    def __hash__(self):
        raise TypeError('IP sets are unhashable!')

    def __contains__(self, ip):
        # Iterating over self._cidrs is an O(n) operation: 1000 items in
        # self._cidrs would mean 1000 loops. Iterating over all possible
        # supernets loops at most 32 times for IPv4 or 128 times for IPv6,
        # no matter how many CIDRs this object contains.
        supernet = IPNetwork(ip)
        if supernet in self._cidrs:
            return True
        while supernet._prefixlen:
            supernet._prefixlen -= 1
            if supernet in self._cidrs:
                return True
        return False

    def __nonzero__(self):
        return bool(self._cidrs)

    __bool__ = __nonzero__  #   Python 3.x.

    def __iter__(self):
        return _itertools.chain(*sorted(self._cidrs))

    def iter_cidrs(self):
        return sorted(self._cidrs)

    def add(self, addr, flags=0):
        if isinstance(addr, IPRange):
            new_cidrs = dict.fromkeys(
                iprange_to_cidrs(addr[0], addr[-1]), True)
            self._cidrs.update(new_cidrs)
            self.compact()
            return
        if isinstance(addr, IPNetwork):
            # Networks like 10.1.2.3/8 need to be normalized to 10.0.0.0/8
            addr = addr.cidr
        elif isinstance(addr, _int_type):
            addr = IPNetwork(IPAddress(addr, flags=flags))
        else:
            addr = IPNetwork(addr)

        self._cidrs[addr] = True
        self._compact_single_network(addr)

    def remove(self, addr, flags=0):
        if isinstance(addr, IPRange):
            cidrs = iprange_to_cidrs(addr[0], addr[-1])
            for cidr in cidrs:
                self.remove(cidr)
            return

        if isinstance(addr, _int_type):
            addr = IPAddress(addr, flags=flags)
        else:
            addr = IPNetwork(addr)

        #   This add() is required for address blocks provided that are larger
        #   than blocks found within the set but have overlaps. e.g. :-
        #
        #   >>> IPSet(['192.0.2.0/24']).remove('192.0.2.0/23')
        #   IPSet([])
        #
        self.add(addr)

        remainder = None
        matching_cidr = None

        #   Search for a matching CIDR and exclude IP from it.
        for cidr in self._cidrs:
            if addr in cidr:
                remainder = cidr_exclude(cidr, addr)
                matching_cidr = cidr
                break

        #   Replace matching CIDR with remaining CIDR elements.
        if remainder is not None:
            del self._cidrs[matching_cidr]
            for cidr in remainder:
                self._cidrs[cidr] = True
                # No call to self.compact() is needed. Removing an IPNetwork cannot
                # create mergable networks.

    def pop(self):
        return self._cidrs.popitem()[0]

    def isdisjoint(self, other):
        result = self.intersection(other)
        return not result

    def copy(self):
        obj_copy = self.__class__()
        obj_copy._cidrs.update(self._cidrs)
        return obj_copy

    def update(self, iterable, flags=0):
        if isinstance(iterable, IPSet):
            self._cidrs = dict.fromkeys(
                (ip for ip in cidr_merge(_dict_keys(self._cidrs)
                                         + _dict_keys(iterable._cidrs))), True)
            return
        elif isinstance(iterable, (IPNetwork, IPRange)):
            self.add(iterable)
            return

        if not hasattr(iterable, '__iter__'):
            raise TypeError('an iterable was expected!')
        #   An iterable containing IP addresses or subnets.
        mergeable = []
        for addr in iterable:
            if isinstance(addr, _int_type):
                addr = IPAddress(addr, flags=flags)
            mergeable.append(addr)

        for cidr in cidr_merge(_dict_keys(self._cidrs) + mergeable):
            self._cidrs[cidr] = True

        self.compact()

    def clear(self):
        self._cidrs = {}

    def __eq__(self, other):
        try:
            return self._cidrs == other._cidrs
        except AttributeError:
            return NotImplemented

    def __ne__(self, other):
        try:
            return self._cidrs != other._cidrs
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        if not hasattr(other, '_cidrs'):
            return NotImplemented

        return self.size < other.size and self.issubset(other)

    def issubset(self, other):
        for cidr in self._cidrs:
            if cidr not in other:
                return False
        return True

    __le__ = issubset

    def __gt__(self, other):
        if not hasattr(other, '_cidrs'):
            return NotImplemented

        return self.size > other.size and self.issuperset(other)

    def issuperset(self, other):
        if not hasattr(other, '_cidrs'):
            return NotImplemented

        for cidr in other._cidrs:
            if cidr not in self:
                return False
        return True

    __ge__ = issuperset

    def union(self, other):
        ip_set = self.copy()
        ip_set.update(other)
        return ip_set

    __or__ = union

    def intersection(self, other):
        result_cidrs = {}

        own_nets = sorted(self._cidrs)
        other_nets = sorted(other._cidrs)
        own_idx = 0
        other_idx = 0
        own_len = len(own_nets)
        other_len = len(other_nets)
        while own_idx < own_len and other_idx < other_len:
            own_cur = own_nets[own_idx]
            other_cur = other_nets[other_idx]

            if own_cur == other_cur:
                result_cidrs[own_cur] = True
                own_idx += 1
                other_idx += 1
            elif own_cur in other_cur:
                result_cidrs[own_cur] = True
                own_idx += 1
            elif other_cur in own_cur:
                result_cidrs[other_cur] = True
                other_idx += 1
            else:
                # own_cur and other_cur have nothing in common
                if own_cur < other_cur:
                    own_idx += 1
                else:
                    other_idx += 1

        # We ran out of networks in own_nets or other_nets. Either way, there
        # can be no further result_cidrs.
        result = IPSet()
        result._cidrs = result_cidrs
        return result

    __and__ = intersection

    def symmetric_difference(self, other):
        # In contrast to intersection() and difference(), we cannot construct
        # the result_cidrs easily. Some cidrs may have to be merged, e.g. for
        # IPSet(["10.0.0.0/32"]).symmetric_difference(IPSet(["10.0.0.1/32"])).
        result_ranges = []

        own_nets = sorted(self._cidrs)
        other_nets = sorted(other._cidrs)
        own_idx = 0
        other_idx = 0
        own_len = len(own_nets)
        other_len = len(other_nets)
        while own_idx < own_len and other_idx < other_len:
            own_cur = own_nets[own_idx]
            other_cur = other_nets[other_idx]

            if own_cur == other_cur:
                own_idx += 1
                other_idx += 1
            elif own_cur in other_cur:
                own_idx = _subtract(other_cur, own_nets, own_idx, result_ranges)
                other_idx += 1
            elif other_cur in own_cur:
                other_idx = _subtract(own_cur, other_nets, other_idx, result_ranges)
                own_idx += 1
            else:
                # own_cur and other_cur have nothing in common
                if own_cur < other_cur:
                    result_ranges.append((own_cur._module.version,
                                          own_cur.first, own_cur.last))
                    own_idx += 1
                else:
                    result_ranges.append((other_cur._module.version,
                                          other_cur.first, other_cur.last))
                    other_idx += 1

        # If the above loop terminated because it processed all cidrs of
        # "other", then any remaining cidrs in self must be part of the result.
        while own_idx < own_len:
            own_cur = own_nets[own_idx]
            result_ranges.append((own_cur._module.version,
                                  own_cur.first, own_cur.last))
            own_idx += 1

        # If the above loop terminated because it processed all cidrs of
        # self, then any remaining cidrs in "other" must be part of the result.
        while other_idx < other_len:
            other_cur = other_nets[other_idx]
            result_ranges.append((other_cur._module.version,
                                  other_cur.first, other_cur.last))
            other_idx += 1

        result = IPSet()
        for start, stop in _iter_merged_ranges(result_ranges):
            cidrs = iprange_to_cidrs(start, stop)
            for cidr in cidrs:
                result._cidrs[cidr] = True
        return result

    __xor__ = symmetric_difference

    def difference(self, other):
        result_ranges = []
        result_cidrs = {}

        own_nets = sorted(self._cidrs)
        other_nets = sorted(other._cidrs)
        own_idx = 0
        other_idx = 0
        own_len = len(own_nets)
        other_len = len(other_nets)
        while own_idx < own_len and other_idx < other_len:
            own_cur = own_nets[own_idx]
            other_cur = other_nets[other_idx]

            if own_cur == other_cur:
                own_idx += 1
                other_idx += 1
            elif own_cur in other_cur:
                own_idx += 1
            elif other_cur in own_cur:
                other_idx = _subtract(own_cur, other_nets, other_idx,
                                      result_ranges)
                own_idx += 1
            else:
                # own_cur and other_cur have nothing in common
                if own_cur < other_cur:
                    result_cidrs[own_cur] = True
                    own_idx += 1
                else:
                    other_idx += 1

        # If the above loop terminated because it processed all cidrs of
        # "other", then any remaining cidrs in self must be part of the result.
        while own_idx < own_len:
            result_cidrs[own_nets[own_idx]] = True
            own_idx += 1

        for start, stop in _iter_merged_ranges(result_ranges):
            for cidr in iprange_to_cidrs(start, stop):
                result_cidrs[cidr] = True

        result = IPSet()
        result._cidrs = result_cidrs
        return result

    __sub__ = difference

    def __len__(self):
        size = self.size
        if size > _sys_maxint:
            raise IndexError(
                "range contains more than %d (sys.maxint) IP addresses!"
                "Use the .size property instead." % _sys_maxint)
        return size

    @property
    def size(self):
        return sum([cidr.size for cidr in self._cidrs])

    def __repr__(self):
        return 'IPSet(%r)' % [str(c) for c in sorted(self._cidrs)]

    __str__ = __repr__

    def iscontiguous(self):
        cidrs = self.iter_cidrs()
        if len(cidrs) > 1:
            previous = cidrs[0][0]
            for cidr in cidrs:
                if cidr[0] != previous:
                    return False
                previous = cidr[-1] + 1
        return True

    def iprange(self):
        if self.iscontiguous():
            cidrs = self.iter_cidrs()
            if not cidrs:
                return None
            return IPRange(cidrs[0][0], cidrs[-1][-1])
        else:
            raise ValueError("IPSet is not contiguous")

    def iter_ipranges(self):
        sorted_ranges = [(cidr._module.version, cidr.first, cidr.last) for
                         cidr in self.iter_cidrs()]

        for start, stop in _iter_merged_ranges(sorted_ranges):
            yield IPRange(start, stop)
