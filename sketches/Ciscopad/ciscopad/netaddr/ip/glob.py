def valid_glob(ipglob):
    #TODO: Add support for abbreviated ipglobs.
    #TODO: e.g. 192.0.*.* == 192.0.*
    #TODO:      *.*.*.*     == *
    #TODO: Add strict flag to enable verbose ipglob checking.
    if not _is_str(ipglob):
        return False

    seen_hyphen = False
    seen_asterisk = False

    octets = ipglob.split('.')

    if len(octets) != 4:
        return False

    for octet in octets:
        if '-' in octet:
            if seen_hyphen:
                return False
            seen_hyphen = True
            if seen_asterisk:
                #   Asterisks cannot precede hyphenated octets.
                return False
            try:
                (octet1, octet2) = [int(i) for i in octet.split('-')]
            except ValueError:
                return False
            if octet1 >= octet2:
                return False
            if not 0 <= octet1 <= 254:
                return False
            if not 1 <= octet2 <= 255:
                return False
        elif octet == '*':
            seen_asterisk = True
        else:
            if seen_hyphen is True:
                return False
            if seen_asterisk is True:
                return False
            try:
                if not 0 <= int(octet) <= 255:
                    return False
            except ValueError:
                return False
    return True


def glob_to_iptuple(ipglob):
    if not valid_glob(ipglob):
        raise AddrFormatError('not a recognised IP glob range: %r!' % (ipglob,))

    start_tokens = []
    end_tokens = []

    for octet in ipglob.split('.'):
        if '-' in octet:
            tokens = octet.split('-')
            start_tokens.append(tokens[0])
            end_tokens.append(tokens[1])
        elif octet == '*':
            start_tokens.append('0')
            end_tokens.append('255')
        else:
            start_tokens.append(octet)
            end_tokens.append(octet)

    return IPAddress('.'.join(start_tokens)), IPAddress('.'.join(end_tokens))


def glob_to_iprange(ipglob):
    if not valid_glob(ipglob):
        raise AddrFormatError('not a recognised IP glob range: %r!' % (ipglob,))

    start_tokens = []
    end_tokens = []

    for octet in ipglob.split('.'):
        if '-' in octet:
            tokens = octet.split('-')
            start_tokens.append(tokens[0])
            end_tokens.append(tokens[1])
        elif octet == '*':
            start_tokens.append('0')
            end_tokens.append('255')
        else:
            start_tokens.append(octet)
            end_tokens.append(octet)

    return IPRange('.'.join(start_tokens), '.'.join(end_tokens))


def iprange_to_globs(start, end):
    start = IPAddress(start)
    end = IPAddress(end)

    if start.version != 4 and end.version != 4:
        raise AddrConversionError('IP glob ranges only support IPv4!')

    def _iprange_to_glob(lb, ub):
        #   Internal function to process individual IP globs.
        t1 = [int(_) for _ in str(lb).split('.')]
        t2 = [int(_) for _ in str(ub).split('.')]

        tokens = []

        seen_hyphen = False
        seen_asterisk = False

        for i in range(4):
            if t1[i] == t2[i]:
                #   A normal octet.
                tokens.append(str(t1[i]))
            elif (t1[i] == 0) and (t2[i] == 255):
                #   An asterisk octet.
                tokens.append('*')
                seen_asterisk = True
            else:
                #   Create a hyphenated octet - only one allowed per IP glob.
                if not seen_asterisk:
                    if not seen_hyphen:
                        tokens.append('%s-%s' % (t1[i], t2[i]))
                        seen_hyphen = True
                    else:
                        raise AddrConversionError(
                            'only 1 hyphenated octet per IP glob allowed!')
                else:
                    raise AddrConversionError(
                        "asterisks are not allowed before hyphenated octets!")

        return '.'.join(tokens)

    globs = []

    try:
        #   IP range can be represented by a single glob.
        ipglob = _iprange_to_glob(start, end)
        if not valid_glob(ipglob):
            #TODO: this is a workaround, it is produces non-optimal but valid
            #TODO: glob conversions. Fix inner function so that is always
            #TODO: produces a valid glob.
            raise AddrConversionError('invalid ip glob created')
        globs.append(ipglob)
    except AddrConversionError:
        #   Break IP range up into CIDRs before conversion to globs.
        #
        #TODO: this is still not completely optimised but is good enough
        #TODO: for the moment.
        #
        for cidr in iprange_to_cidrs(start, end):
            ipglob = _iprange_to_glob(cidr[0], cidr[-1])
            globs.append(ipglob)

    return globs


def glob_to_cidrs(ipglob):
    return iprange_to_cidrs(*glob_to_iptuple(ipglob))


def cidr_to_glob(cidr):
    ip = IPNetwork(cidr)
    globs = iprange_to_globs(ip[0], ip[-1])
    if len(globs) != 1:
        #   There should only ever be a one to one mapping between a CIDR and
        #   an IP glob range.
        raise AddrConversionError('bad CIDR to IP glob conversion!')
    return globs[0]


class IPGlob(IPRange):
    __slots__ = ('_glob',)

    def __init__(self, ipglob):
        (start, end) = glob_to_iptuple(ipglob)
        super(IPGlob, self).__init__(start, end)
        self.glob = iprange_to_globs(self._start, self._end)[0]

    def __getstate__(self):
        return super(IPGlob, self).__getstate__()

    def __setstate__(self, state):
        super(IPGlob, self).__setstate__(state)
        self.glob = iprange_to_globs(self._start, self._end)[0]

    def _get_glob(self):
        return self._glob

    def _set_glob(self, ipglob):
        (self._start, self._end) = glob_to_iptuple(ipglob)
        self._glob = iprange_to_globs(self._start, self._end)[0]

    glob = property(_get_glob, _set_glob, None,
        'an arbitrary IP address range in glob format.')

    def __str__(self):
        return "%s" % self.glob

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.glob)
