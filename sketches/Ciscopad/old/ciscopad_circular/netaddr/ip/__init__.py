import sys as _sys

from netaddr.core import AddrFormatError, AddrConversionError, num_bits, \
    DictDotLookup, NOHOST, N, INET_PTON, P, ZEROFILL, Z

from netaddr.strategy import ipv4 as _ipv4

from netaddr.compat import _sys_maxint, _iter_next, _iter_range, _is_str, _int_type, \
    _str_type

class BaseIP(object):
    __slots__ = ('_value', '_module', '__weakref__')

    def __init__(self):
        self._value = None
        self._module = None

    def _set_value(self, value):
        if not isinstance(value, _int_type):
            raise TypeError('int argument expected, not %s' % type(value))
        if not 0 <= value <= self._module.max_int:
            raise AddrFormatError('value out of bounds for an %s address!' \
                % self._module.family_name)
        self._value = value

    value = property(lambda self: self._value, _set_value,
        doc='a positive integer representing the value of IP address/subnet.')

    def key(self):
        return NotImplemented

    def sort_key(self):
        return NotImplemented

    def __hash__(self):
        return hash(self.key())

    def __eq__(self, other):
        try:
            return self.key() == other.key()
        except (AttributeError, TypeError):
            return NotImplemented

    def __ne__(self, other):
        try:
            return self.key() != other.key()
        except (AttributeError, TypeError):
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.sort_key() < other.sort_key()
        except (AttributeError, TypeError):
            return NotImplemented

    def __le__(self, other):
        try:
            return self.sort_key() <= other.sort_key()
        except (AttributeError, TypeError):
            return NotImplemented

    def __gt__(self, other):
        try:
            return self.sort_key() > other.sort_key()
        except (AttributeError, TypeError):
            return NotImplemented

    def __ge__(self, other):
        try:
            return self.sort_key() >= other.sort_key()
        except (AttributeError, TypeError):
            return NotImplemented

    def is_unicast(self):
        return not self.is_multicast()

    def is_multicast(self):
        if self._module == _ipv4:
            return self in IPV4_MULTICAST

    def is_loopback(self):
        if self._module.version == 4:
            return self in IPV4_LOOPBACK

    def is_private(self):
        if self._module.version == 4:
            for cidr in IPV4_PRIVATE:
                if self in cidr:
                    return True

        if self.is_link_local():
            return True

        return False

    def is_link_local(self):
        if self._module.version == 4:
            return self in IPV4_LINK_LOCAL

    def is_reserved(self):
        if self._module.version == 4:
            for cidr in IPV4_RESERVED:
                if self in cidr:
                    return True
        return False

    @property
    def info(self):
        #   Lazy loading of IANA data structures.
        from netaddr.ip.iana import query
        return DictDotLookup(query(self))

    @property
    def version(self):
        return self._module.version


class IPAddress(BaseIP):
    __slots__ = ()

    def __init__(self, addr, version=None, flags=0):
        super(IPAddress, self).__init__()

        if isinstance(addr, BaseIP):
            #   Copy constructor.
            if version is not None and version != addr._module.version:
                raise ValueError('cannot switch IP versions using '
                    'copy constructor!')
            self._value = addr._value
            self._module = addr._module
        else:
            #   Explicit IP address version.
            if version is not None:
                if version == 4:
                    self._module = _ipv4
                else:
                    raise ValueError('%r is an invalid IP version!' % version)

            if _is_str(addr) and '/' in addr:
                raise ValueError('%s() does not support netmasks or subnet' \
                    ' prefixes! See documentation for details.'
                    % self.__class__.__name__)

            if self._module is None:
                #   IP version is implicit, detect it from addr.
                if isinstance(addr, _int_type):
                    try:
                        if 0 <= int(addr) <= _ipv4.max_int:
                            self._value = int(addr)
                            self._module = _ipv4
                    except ValueError:
                        pass
                else:
                    for module in _ipv4:
                        try:
                            self._value = module.str_to_int(addr, flags)
                        except:
                            continue
                        else:
                            self._module = module
                            break

                if self._module is None:
                    raise AddrFormatError('failed to detect a valid IP ' \
                        'address from %r' % addr)
            else:
                #   IP version is explicit.
                if _is_str(addr):
                    try:
                        self._value = self._module.str_to_int(addr, flags)
                    except AddrFormatError:
                        raise AddrFormatError('base address %r is not IPv%d'
                            % (addr, self._module.version))
                else:
                    if 0 <= int(addr) <= self._module.max_int:
                        self._value = int(addr)
                    else:
                        raise AddrFormatError('bad address format: %r' % (addr,))

    def __getstate__(self):
        return self._value, self._module.version

    def __setstate__(self, state):
        value, version = state

        self._value = value

        if version == 4:
            self._module = _ipv4
        else:
            raise ValueError('unpickling failed for object state: %s' \
                % str(state))

    def netmask_bits(self):
        if not self.is_netmask():
            return self._module.width

        # the '0' address (e.g. 0.0.0.0 or 0000::) is a valid netmask with
        # no bits set.
        if self._value == 0:
            return 0

        i_val = self._value
        numbits = 0

        while i_val > 0:
            if i_val & 1 == 1:
                break
            numbits += 1
            i_val >>= 1

        mask_length = self._module.width - numbits

        if not 0 <= mask_length <= self._module.width:
            raise ValueError('Unexpected mask length %d for address type!' \
                % mask_length)

        return mask_length

    def is_hostmask(self):
        int_val = self._value + 1
        return (int_val & (int_val - 1) == 0)

    def is_netmask(self):
        int_val = (self._value ^ self._module.max_int) + 1
        return (int_val & (int_val - 1) == 0)

    def __iadd__(self, num):
        new_value = int(self._value + num)
        if 0 <= new_value <= self._module.max_int:
            self._value = new_value
            return self
        raise IndexError('result outside valid IP address boundary!')

    def __isub__(self, num):
        new_value = int(self._value - num)
        if 0 <= new_value <= self._module.max_int:
            self._value = new_value
            return self
        raise IndexError('result outside valid IP address boundary!')

    def __add__(self, num):
        new_value = int(self._value + num)
        if 0 <= new_value <= self._module.max_int:
            return self.__class__(new_value, self._module.version)
        raise IndexError('result outside valid IP address boundary!')

    __radd__ = __add__

    def __sub__(self, num):
        new_value = int(self._value - num)
        if 0 <= new_value <= self._module.max_int:
            return self.__class__(new_value, self._module.version)
        raise IndexError('result outside valid IP address boundary!')

    def __rsub__(self, num):
        new_value = int(num - self._value)
        if 0 <= new_value <= self._module.max_int:
            return self.__class__(new_value, self._module.version)
        raise IndexError('result outside valid IP address boundary!')

    def key(self):
        #   NB - we return the value here twice because this IP Address may
        #   be sorted with a list of networks and it should still end up
        #   in the expected order.
        return self._module.version, self._value

    def sort_key(self):
        return self._module.version, self._value, self._module.width

    def __int__(self):
        return self._value

    def __long__(self):
        return self._value

    def __oct__(self):
        #   Python 2.x
        if self._value == 0:
            return '0'
        return '0%o' % self._value

    def __hex__(self):
        #   Python 2.x
        return '0x%x' % self._value

    def __index__(self):
        #   Python 3.x
        return self._value

    def __bytes__(self):
        #   Python 3.x
        return self._value.to_bytes(self._module.width//8, 'big')

    def bits(self, word_sep=None):
        return self._module.int_to_bits(self._value, word_sep)

    @property
    def packed(self):
        return self._module.int_to_packed(self._value)

    @property
    def words(self):
        return self._module.int_to_words(self._value)

    @property
    def bin(self):
        return self._module.int_to_bin(self._value)

    @property
    def reverse_dns(self):
        return self._module.int_to_arpa(self._value)

    def __or__(self, other):
        return self.__class__(self._value | int(other), self._module.version)

    def __and__(self, other):
        return self.__class__(self._value & int(other), self._module.version)

    def __xor__(self, other):
        return self.__class__(self._value ^ int(other), self._module.version)

    def __lshift__(self, numbits):
        return self.__class__(self._value << numbits, self._module.version)

    def __rshift__(self, numbits):
        return self.__class__(self._value >> numbits, self._module.version)

    def __nonzero__(self):
        #   Python 2.x.
        return bool(self._value)
    __bool__ = __nonzero__  #   Python 3.x.

    def __str__(self):
        return self._module.int_to_str(self._value)

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self)


class IPListMixin(object):
    __slots__ = ()
    def __iter__(self):
        start_ip = IPAddress(self.first, self._module.version)
        end_ip = IPAddress(self.last, self._module.version)
        return iter_iprange(start_ip, end_ip)

    @property
    def size(self):
        return int(self.last - self.first + 1)

    def __len__(self):
        size = self.size
        if size > _sys_maxint:
            raise IndexError(("range contains more than %d (sys.maxint) "
               "IP addresses! Use the .size property instead." % _sys_maxint))
        return size

    def __getitem__(self, index):
        item = None

        if hasattr(index, 'indices'):
            if self._module.version == 6:
                raise TypeError('IPv6 slices are not supported!')

            (start, stop, step) = index.indices(self.size)

            if (start + step < 0) or (step > stop):
                #   step value exceeds start and stop boundaries.
                item = iter([IPAddress(self.first, self._module.version)])
            else:
                start_ip = IPAddress(self.first + start, self._module.version)
                end_ip = IPAddress(self.first + stop - step, self._module.version)
                item = iter_iprange(start_ip, end_ip, step)
        else:
            try:
                index = int(index)
                if (- self.size) <= index < 0:
                    #   negative index.
                    item = IPAddress(self.last + index + 1, self._module.version)
                elif 0 <= index <= (self.size - 1):
                    #   Positive index or zero index.
                    item = IPAddress(self.first + index, self._module.version)
                else:
                    raise IndexError('index out range for address range size!')
            except ValueError:
                raise TypeError('unsupported index type %r!' % index)

        return item

    def __contains__(self, other):
        if isinstance(other, BaseIP):
            if self._module.version != other._module.version:
                return False
            if isinstance(other, IPAddress):
                return other._value >= self.first and other._value <= self.last
            # Assume that we (and the other) provide .first and .last.
            return other.first >= self.first and other.last <= self.last

        # Whatever it is, try to interpret it as IPAddress.
        return IPAddress(other) in self

    def __nonzero__(self):
        #   Python 2.x.
        return True

    __bool__ = __nonzero__  #   Python 3.x.


def parse_ip_network(module, addr, implicit_prefix=False, flags=0):
    if isinstance(addr, tuple):
        #   CIDR integer tuple
        if len(addr) != 2:
            raise AddrFormatError('invalid %s tuple!' % module.family_name)
        value, prefixlen = addr

        if not(0 <= value <= module.max_int):
            raise AddrFormatError('invalid address value for %s tuple!'
                % module.family_name)
        if not(0 <= prefixlen <= module.width):
            raise AddrFormatError('invalid prefix for %s tuple!' \
                % module.family_name)
    elif isinstance(addr, _str_type):
        #   CIDR-like string subnet
        if implicit_prefix:
            #TODO: deprecate this option in netaddr 0.8.x
            addr = cidr_abbrev_to_verbose(addr)

        if '/' in addr:
            val1, val2 = addr.split('/', 1)
        else:
            val1 = addr
            val2 = None

        try:
            ip = IPAddress(val1, module.version, flags=INET_PTON)
        except AddrFormatError:
            if module.version == 4:
                #   Try a partial IPv4 network address...
                expanded_addr = _ipv4.expand_partial_address(val1)
                ip = IPAddress(expanded_addr, module.version, flags=INET_PTON)
            else:
                raise AddrFormatError('invalid IPNetwork address %s!' % addr)
        value = ip._value

        try:
            #   Integer CIDR prefix.
            prefixlen = int(val2)
        except TypeError:
            if val2 is None:
                #   No prefix was specified.
                prefixlen = module.width
        except ValueError:
            #   Not an integer prefix, try a netmask/hostmask prefix.
            mask = IPAddress(val2, module.version, flags=INET_PTON)
            if mask.is_netmask():
                prefixlen = module.netmask_to_prefix[mask._value]
            elif mask.is_hostmask():
                prefixlen = module.hostmask_to_prefix[mask._value]
            else:
                raise AddrFormatError('addr %r is not a valid IPNetwork!' \
                    % addr)

        if not 0 <= prefixlen <= module.width:
            raise AddrFormatError('invalid prefix for %s address!' \
                % module.family_name)
    else:
        raise TypeError('unexpected type %s for addr arg' % type(addr))

    if flags & NOHOST:
        #   Remove host bits.
        netmask = module.prefix_to_netmask[prefixlen]
        value = value & netmask

    return value, prefixlen


class IPNetwork(BaseIP, IPListMixin):
    __slots__ = ('_prefixlen',)

    def __init__(self, addr, implicit_prefix=False, version=None, flags=0):
        super(IPNetwork, self).__init__()

        value, prefixlen, module = None, None, None

        if hasattr(addr, '_prefixlen'):
            #   IPNetwork object copy constructor
            value = addr._value
            module = addr._module
            prefixlen = addr._prefixlen
        elif hasattr(addr, '_value'):
            #   IPAddress object copy constructor
            value = addr._value
            module = addr._module
            prefixlen = module.width
        elif version == 4:
            value, prefixlen = parse_ip_network(_ipv4, addr,
                implicit_prefix=implicit_prefix, flags=flags)
            module = _ipv4
        else:
            if version is not None:
                raise ValueError('%r is an invalid IP version!' % version)
            try:
                module = _ipv4
                value, prefixlen = parse_ip_network(module, addr,
                    implicit_prefix, flags)
            except AddrFormatError:
                try:
                    module = _ipv6
                    value, prefixlen = parse_ip_network(module, addr,
                        implicit_prefix, flags)
                except AddrFormatError:
                    pass

                if value is None:
                    raise AddrFormatError('invalid IPNetwork %s' % (addr,))

        self._value = value
        self._prefixlen = prefixlen
        self._module = module

    def __getstate__(self):
        return self._value, self._prefixlen, self._module.version

    def __setstate__(self, state):
        value, prefixlen, version = state

        self._value = value

        if version == 4:
            self._module = _ipv4
        else:
            raise ValueError('unpickling failed for object state %s' \
                % (state,))

        if 0 <= prefixlen <= self._module.width:
            self._prefixlen = prefixlen
        else:
            raise ValueError('unpickling failed for object state %s' \
                % (state,))

    def _set_prefixlen(self, value):
        if not isinstance(value, _int_type):
            raise TypeError('int argument expected, not %s' % type(value))
        if not 0 <= value <= self._module.width:
            raise AddrFormatError('invalid prefix for an %s address!' \
                % self._module.family_name)
        self._prefixlen = value

    prefixlen = property(lambda self: self._prefixlen, _set_prefixlen,
        doc='size of the bitmask used to separate the network from the host bits')

    @property
    def ip(self):
        return IPAddress(self._value, self._module.version)

    @property
    def network(self):
        return IPAddress(self._value & self._netmask_int, self._module.version)

    @property
    def broadcast(self):
        if self._module.version == 4 and (self._module.width - self._prefixlen) <= 1:
            return None
        else:
            return IPAddress(self._value | self._hostmask_int, self._module.version)

    @property
    def first(self):
        return self._value & (self._module.max_int ^ self._hostmask_int)

    @property
    def last(self):
        hostmask = (1 << (self._module.width - self._prefixlen)) - 1
        return self._value | hostmask

    @property
    def netmask(self):
        netmask = self._module.max_int ^ self._hostmask_int
        return IPAddress(netmask, self._module.version)

    @netmask.setter
    def netmask(self, value):
        ip = IPAddress(value)

        if ip.version != self.version:
            raise ValueError("IP version mismatch: %s and %s" % (ip, self))

        if not ip.is_netmask():
            raise ValueError("Invalid subnet mask specified: %s" % str(value))

        self.prefixlen = ip.netmask_bits()

    @property
    def _netmask_int(self):
        return self._module.max_int ^ self._hostmask_int

    @property
    def hostmask(self):
        hostmask = (1 << (self._module.width - self._prefixlen)) - 1
        return IPAddress(hostmask, self._module.version)

    @property
    def _hostmask_int(self):
        return (1 << (self._module.width - self._prefixlen)) - 1

    @property
    def cidr(self):
        return IPNetwork(
                (self._value & self._netmask_int, self._prefixlen),
                version=self._module.version)

    def __iadd__(self, num):
        new_value = int(self.network) + (self.size * num)

        if (new_value + (self.size - 1)) > self._module.max_int:
            raise IndexError('increment exceeds address boundary!')
        if new_value < 0:
            raise IndexError('increment is less than zero!')

        self._value = new_value
        return self

    def __isub__(self, num):
        new_value = int(self.network) - (self.size * num)

        if new_value < 0:
            raise IndexError('decrement is less than zero!')
        if (new_value + (self.size - 1)) > self._module.max_int:
            raise IndexError('decrement exceeds address boundary!')

        self._value = new_value
        return self

    def __contains__(self, other):
        if isinstance(other, BaseIP):
            if self._module.version != other._module.version:
                return False

            # self_net will contain only the network bits.
            shiftwidth = self._module.width - self._prefixlen
            self_net = self._value >> shiftwidth
            if isinstance(other, IPRange):
                # IPRange has no _value.
                # (self_net+1)<<shiftwidth is not our last address, but the one
                # after the last one.
                return ((self_net << shiftwidth) <= other._start._value and
                        (((self_net + 1) << shiftwidth) > other._end._value))

            other_net = other._value >> shiftwidth
            if isinstance(other, IPAddress):
                return other_net == self_net
            if isinstance(other, IPNetwork):
                return self_net == other_net and self._prefixlen <= other._prefixlen

        # Whatever it is, try to interpret it as IPNetwork
        return IPNetwork(other) in self

    def key(self):
        return self._module.version, self.first, self.last

    def sort_key(self):
        net_size_bits = self._prefixlen - 1
        first = self._value & (self._module.max_int ^ self._hostmask_int)
        host_bits = self._value - first
        return self._module.version, first, net_size_bits, host_bits

    def previous(self, step=1):
        ip_copy = self.__class__('%s/%d' % (self.network, self.prefixlen),
            self._module.version)
        ip_copy -= step
        return ip_copy

    def next(self, step=1):
        ip_copy = self.__class__('%s/%d' % (self.network, self.prefixlen),
            self._module.version)
        ip_copy += step
        return ip_copy

    def supernet(self, prefixlen=0):
        if not 0 <= prefixlen <= self._module.width:
            raise ValueError('CIDR prefix /%d invalid for IPv%d!' \
                % (prefixlen, self._module.version))

        supernets = []
        # Use a copy of self as we'll be editing it.
        supernet = self.cidr
        supernet._prefixlen = prefixlen
        while supernet._prefixlen != self._prefixlen:
            supernets.append(supernet.cidr)
            supernet._prefixlen += 1
        return supernets

    def subnet(self, prefixlen, count=None, fmt=None):
        if not 0 <= self.prefixlen <= self._module.width:
            raise ValueError('CIDR prefix /%d invalid for IPv%d!' \
                % (prefixlen, self._module.version))

        if not self.prefixlen <= prefixlen:
            #   Don't return anything.
            return

        #   Calculate number of subnets to be returned.
        width = self._module.width
        max_subnets = 2 ** (width - self.prefixlen) // 2 ** (width - prefixlen)

        if count is None:
            count = max_subnets

        if not 1 <= count <= max_subnets:
            raise ValueError('count outside of current IP subnet boundary!')

        base_subnet = self._module.int_to_str(self.first)
        i = 0
        while(i < count):
            subnet = self.__class__('%s/%d' % (base_subnet, prefixlen),
                self._module.version)
            subnet.value += (subnet.size * i)
            subnet.prefixlen = prefixlen
            i += 1
            yield subnet

    def iter_hosts(self):
        it_hosts = iter([])

        #   IPv4 logic.
        it_hosts = iter_iprange(IPAddress(self.first, self._module.version),
                                IPAddress(self.last, self._module.version))
        return it_hosts

    def __str__(self):
        addr = self._module.int_to_str(self._value)
        return "%s/%s" % (addr, self.prefixlen)

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self)


class IPRange(BaseIP, IPListMixin):
    __slots__ = ('_start', '_end')

    def __init__(self, start, end, flags=0):
        self._start = IPAddress(start, flags=flags)
        self._module = self._start._module
        self._end = IPAddress(end, self._module.version, flags=flags)
        if int(self._start) > int(self._end):
            raise AddrFormatError('lower bound IP greater than upper bound!')

    def __getstate__(self):
        return self._start.value, self._end.value, self._module.version

    def __setstate__(self, state):
        start, end, version = state

        self._start = IPAddress(start, version)
        self._module = self._start._module
        self._end = IPAddress(end, version)

    def __contains__(self, other):
        if isinstance(other, BaseIP):
            if self._module.version != other._module.version:
                return False
            if isinstance(other, IPAddress):
                return (self._start._value <= other._value and
                        self._end._value >= other._value)
            if isinstance(other, IPRange):
                return (self._start._value <= other._start._value and
                        self._end._value >= other._end._value)
            if isinstance(other, IPNetwork):
                shiftwidth = other._module.width - other._prefixlen
                other_start = (other._value >> shiftwidth) << shiftwidth
                # Start of the next network after other
                other_next_start = other_start + (1 << shiftwidth)

                return (self._start._value <= other_start and
                        self._end._value > other_next_start)

        # Whatever it is, try to interpret it as IPAddress.
        return IPAddress(other) in self

    @property
    def first(self):
        return int(self._start)

    @property
    def last(self):
        return int(self._end)

    def key(self):
        return self._module.version, self.first, self.last

    def sort_key(self):
        skey = self._module.width - num_bits(self.size)
        return self._module.version, self._start._value, skey

    def cidrs(self):
        return iprange_to_cidrs(self._start, self._end)

    def __str__(self):
        return "%s-%s" % (self._start, self._end)

    def __repr__(self):
        return "%s('%s', '%s')" % (self.__class__.__name__,
            self._start, self._end)


def iter_unique_ips(*args):
    for cidr in cidr_merge(args):
        for ip in cidr:
            yield ip


def cidr_abbrev_to_verbose(abbrev_cidr):
    #   Internal function that returns a prefix value based on the old IPv4
    #   classful network scheme that has been superseded (almost) by CIDR.
    def classful_prefix(octet):
        octet = int(octet)
        if not 0 <= octet <= 255:
            raise IndexError('Invalid octet: %r!' % octet)
        if 0 <= octet <= 127:       #   Legacy class 'A' classification.
            return 8
        elif 128 <= octet <= 191:   #   Legacy class 'B' classification.
            return 16
        elif 192 <= octet <= 223:   #   Legacy class 'C' classification.
            return 24
        elif 224 <= octet <= 239:   #   Multicast address range.
            return 4
        return 32                   #   Default.

    if _is_str(abbrev_cidr):
        if ':' in abbrev_cidr or abbrev_cidr == '':
            return abbrev_cidr

    try:
        #   Single octet partial integer or string address.
        i = int(abbrev_cidr)
        return "%s.0.0.0/%s" % (i, classful_prefix(i))
    except ValueError:
        #   Multi octet partial string address with optional prefix.
        if '/' in abbrev_cidr:
            part_addr, prefix = abbrev_cidr.split('/', 1)

            #   Check prefix for validity.
            try:
                if not 0 <= int(prefix) <= 32:
                    raise ValueError('prefixlen in address %r out of range' \
                        ' for IPv4!' % (abbrev_cidr,))
            except ValueError:
                return abbrev_cidr
        else:
            part_addr = abbrev_cidr
            prefix = None

        tokens = part_addr.split('.')
        if len(tokens) > 4:
            #   Not a recognisable format.
            return abbrev_cidr
        for i in range(4 - len(tokens)):
            tokens.append('0')

        if prefix is None:
            try:
                prefix = classful_prefix(tokens[0])
            except ValueError:
                return abbrev_cidr

        return "%s/%s" % ('.'.join(tokens), prefix)
    except (TypeError, IndexError):
        #   Not a recognisable format.
        return abbrev_cidr

def cidr_merge(ip_addrs):
    # The algorithm is quite simple: For each CIDR we create an IP range.
    # Sort them and merge when possible.  Afterwars split them again optimally.
    if not hasattr(ip_addrs, '__iter__'):
        raise ValueError('A sequence or iterator is expected!')

    ranges = []

    for ip in ip_addrs:
        if isinstance(ip, (IPNetwork, IPRange)):
            net = ip
        else:
            net = IPNetwork(ip)
        # Since non-overlapping ranges are the common case, remember the original
        ranges.append( (net.version, net.last, net.first, net) )

    ranges.sort()
    i = len(ranges) - 1
    while i > 0:
        if ranges[i][0] == ranges[i - 1][0] and ranges[i][2] - 1 <= ranges[i - 1][1]:
            ranges[i - 1] = (ranges[i][0], ranges[i][1], min(ranges[i - 1][2], ranges[i][2]))
            del ranges[i]
        i -= 1
    merged = []
    for range_tuple in ranges:
        # If this range wasn't merged we can simply use the old cidr.
        if len(range_tuple) == 4:
            original = range_tuple[3]
            if isinstance(original, IPRange):
                merged.extend(original.cidrs())
            else:
                merged.append(original)
        else:
            version = range_tuple[0]
            range_start = IPAddress(range_tuple[2], version=version)
            range_stop = IPAddress(range_tuple[1], version=version)
            merged.extend(iprange_to_cidrs(range_start, range_stop))
    return merged


def cidr_exclude(target, exclude):
    left, _, right = cidr_partition(target, exclude)

    return left + right

def cidr_partition(target, exclude):
    target = IPNetwork(target)
    exclude = IPNetwork(exclude)

    if exclude.last < target.first:
        #   Exclude subnet's upper bound address less than target
        #   subnet's lower bound.
        return [], [], [target.cidr]
    elif target.last < exclude.first:
        #   Exclude subnet's lower bound address greater than target
        #   subnet's upper bound.
        return [target.cidr], [], []

    if target.prefixlen >= exclude.prefixlen:
        # Exclude contains the target
        return [], [target], []

    left = []
    right = []

    new_prefixlen = target.prefixlen + 1
    # Some @properties that are expensive to get and don't change below.
    target_module_width = target._module.width

    target_first = target.first
    version = exclude.version
    i_lower = target_first
    i_upper = target_first + (2 ** (target_module_width - new_prefixlen))

    while exclude.prefixlen >= new_prefixlen:
        if exclude.first >= i_upper:
            left.append(IPNetwork((i_lower, new_prefixlen), version=version))
            matched = i_upper
        else:
            right.append(IPNetwork((i_upper, new_prefixlen), version=version))
            matched = i_lower

        new_prefixlen += 1

        if new_prefixlen > target_module_width:
            break

        i_lower = matched
        i_upper = matched + (2 ** (target_module_width - new_prefixlen))

    return left, [exclude], right[::-1]


def spanning_cidr(ip_addrs):
    ip_addrs_iter = iter(ip_addrs)
    try:
        network_a = IPNetwork(_iter_next(ip_addrs_iter))
        network_b = IPNetwork(_iter_next(ip_addrs_iter))
    except StopIteration:
        raise ValueError('IP sequence must contain at least 2 elements!')

    if network_a < network_b:
        min_network = network_a
        max_network = network_b
    else:
        min_network = network_b
        max_network = network_a

    for ip in ip_addrs_iter:
        network = IPNetwork(ip)
        if network < min_network:
            min_network = network
        if network > max_network:
            max_network = network

    if min_network.version != max_network.version:
        raise TypeError('IP sequence cannot contain both IPv4 and IPv6!')

    ipnum = max_network.last
    prefixlen = max_network.prefixlen
    lowest_ipnum = min_network.first
    width = max_network._module.width

    while prefixlen > 0 and ipnum > lowest_ipnum:
        prefixlen -= 1
        ipnum &= -(1<<(width-prefixlen))

    return IPNetwork( (ipnum, prefixlen), version=min_network.version )


def iter_iprange(start, end, step=1):
    start = IPAddress(start)
    end = IPAddress(end)

    if start.version != end.version:
        raise TypeError('start and stop IP versions do not match!')
    version = start.version

    step = int(step)
    if step == 0:
        raise ValueError('step argument cannot be zero')

    #   We don't need objects from here, just integers.
    start = int(start)
    stop = int(end)

    negative_step = False

    if step < 0:
        negative_step = True

    index = start - step
    while True:
        index += step
        if negative_step:
            if not index >= stop:
                break
        else:
            if not index <= stop:
                break
        yield IPAddress(index, version)



def iprange_to_cidrs(start, end):
    cidr_list = []

    start = IPNetwork(start)
    end = IPNetwork(end)

    iprange = [start.first, end.last]

    #   Get spanning CIDR covering both addresses.
    cidr_span = spanning_cidr([start, end])
    width = start._module.width

    if cidr_span.first < iprange[0]:
        exclude = IPNetwork((iprange[0]-1, width), version=start.version)
        cidr_list = cidr_partition(cidr_span, exclude)[2]
        cidr_span = cidr_list.pop()
    if cidr_span.last > iprange[1]:
        exclude = IPNetwork((iprange[1]+1, width), version=start.version)
        cidr_list += cidr_partition(cidr_span, exclude)[0]
    else:
        cidr_list.append(cidr_span)

    return cidr_list


def smallest_matching_cidr(ip, cidrs):
    match = None

    if not hasattr(cidrs, '__iter__'):
        raise TypeError('IP address/subnet sequence expected, not %r!'
            % (cidrs,))

    ip = IPAddress(ip)
    for cidr in sorted([IPNetwork(cidr) for cidr in cidrs]):
        if ip in cidr:
            match = cidr
        else:
            if match is not None and cidr.network not in match:
                break

    return match


def largest_matching_cidr(ip, cidrs):
    match = None

    if not hasattr(cidrs, '__iter__'):
        raise TypeError('IP address/subnet sequence expected, not %r!'
            % (cidrs,))

    ip = IPAddress(ip)
    for cidr in sorted([IPNetwork(cidr) for cidr in cidrs]):
        if ip in cidr:
            match = cidr
            break

    return match


def all_matching_cidrs(ip, cidrs):
    matches = []

    if not hasattr(cidrs, '__iter__'):
        raise TypeError('IP address/subnet sequence expected, not %r!'
            % (cidrs,))

    ip = IPAddress(ip)
    for cidr in sorted([IPNetwork(cidr) for cidr in cidrs]):
        if ip in cidr:
            matches.append(cidr)
        else:
            if matches and cidr.network not in matches[-1]:
                break

    return matches

#-----------------------------------------------------------------------------
#   IPv4 address range lookups.
#-----------------------------------------------------------------------------

IPV4_LOOPBACK  = IPNetwork('127.0.0.0/8')    #   Loopback addresses (RFC 990)

IPV4_PRIVATE = (
    IPNetwork('10.0.0.0/8'),        #   Class A private network local communication (RFC 1918)
    IPNetwork('100.64.0.0/10'),     #   Carrier grade NAT (RFC 6598)
    IPNetwork('172.16.0.0/12'),     #   Private network - local communication (RFC 1918)
    IPNetwork('192.0.0.0/24'),      #   IANA IPv4 Special Purpose Address Registry (RFC 5736)
    IPNetwork('192.168.0.0/16'),    #   Class B private network local communication (RFC 1918)
    IPNetwork('198.18.0.0/15'),     #  Testing of inter-network communications between subnets (RFC 2544)
    IPRange('239.0.0.0', '239.255.255.255'),    #   Administrative Multicast
)

IPV4_LINK_LOCAL = IPNetwork('169.254.0.0/16')

IPV4_MULTICAST = IPNetwork('224.0.0.0/4')

IPV4_RESERVED = (
    IPNetwork('0.0.0.0/8'),         #   Broadcast message (RFC 1700)
    IPNetwork('192.0.2.0/24'),      #   TEST-NET examples and documentation (RFC 5737)
    IPNetwork('240.0.0.0/4'),       #   Reserved for  multicast assignments (RFC 5771)
    IPNetwork('198.51.100.0/24'),   #   TEST-NET-2 examples and documentation (RFC 5737)
    IPNetwork('203.0.113.0/24'),    #   TEST-NET-3 examples and documentation (RFC 5737)

    #   Reserved multicast
    IPNetwork('233.252.0.0/24'),    #   Multicast test network
    IPRange('234.0.0.0', '238.255.255.255'),
    IPRange('225.0.0.0', '231.255.255.255'),
) + (IPV4_LOOPBACK, IPV4_6TO4)
