import sys as _sys
import struct as _struct

from ciscopad.netaddr.core import AddrFormatError, ZEROFILL

def _inet_aton(addr):
    return bytes([int(i) for i in addr.split(".")])

#: The width (in bits) of this address type.
width = 32

#: The individual word size (in bits) of this address type.
word_size = 8

#: The AF_* constant value of this address type.
family = "AF_INET"

#: A friendly string name address type.
family_name = "IPv4"

#: The version of this address type.
version = 4

#: The number base to be used when interpreting word values as integers.
word_base = 10

#: The maximum integer value that can be represented by this address type.
max_int = 2 ** width - 1

#: The number of words in this address type.
num_words = width // word_size

#: The maximum integer value for an individual word in this address type.
max_word = 2 ** word_size - 1

#: A dictionary mapping IPv4 CIDR prefixes to the equivalent netmasks.
prefix_to_netmask = dict(
    [(i, max_int ^ (2 ** (width - i) - 1)) for i in range(0, width + 1)])

#: A dictionary mapping IPv4 netmasks to their equivalent CIDR prefixes.
netmask_to_prefix = dict(
    [(max_int ^ (2 ** (width - i) - 1), i) for i in range(0, width + 1)])

#: A dictionary mapping IPv4 CIDR prefixes to the equivalent hostmasks.
prefix_to_hostmask = dict(
    [(i, (2 ** (width - i) - 1)) for i in range(0, width + 1)])

#: A dictionary mapping IPv4 hostmasks to their equivalent CIDR prefixes.
hostmask_to_prefix = dict(
    [((2 ** (width - i) - 1), i) for i in range(0, width + 1)])


def valid_str(addr, flags=0):
    if addr == '':
        raise AddrFormatError('Empty strings are not supported!')

    validity = True

    if flags & ZEROFILL:
        addr = '.'.join(['%d' % int(i) for i in addr.split('.')])

    try:
        if flags & INET_PTON:
            _inet_pton(AF_INET, addr)
        else:
            _inet_aton(addr)
    except Exception:
        validity = False

    return validity


def str_to_int(addr, flags=0):
    if flags & ZEROFILL:
        addr = '.'.join(['%d' % int(i) for i in addr.split('.')])

    try:
        return _struct.unpack('>I', _inet_aton(addr))[0]
    except Exception as e:
        raise e
        #raise AddrFormatError("{} is not a valid IPv4 address string!".format(addr))


def int_to_str(int_val, dialect=None):
    if 0 <= int_val <= max_int:
        return "{}.{}.{}.{}".format(int_val >> 24,
                                   (int_val >> 16) & 0xff,
                                   (int_val >> 8) & 0xff,
                                    int_val & 0xff)
    else:
        raise ValueError('{} is not a valid 32-bit unsigned integer!'.format(int_val))


def int_to_arpa(int_val):
    words = ["{}".format(i) for i in int_to_words(int_val)]
    words.reverse()
    words.extend(['in-addr', 'arpa', ''])
    return '.'.join(words)


def int_to_packed(int_val):
    return _struct.pack('>I', int_val)


def packed_to_int(packed_int):
    return _struct.unpack('>I', packed_int)[0]


def valid_words(words):
    return _valid_words(words, word_size, num_words)


def int_to_words(int_val):
    if not 0 <= int_val <= max_int:
        raise ValueError('%r is not a valid integer value supported by'
                         'this address type!' % (int_val,))
    return ( int_val >> 24,
            (int_val >> 16) & 0xff,
            (int_val >>  8) & 0xff,
             int_val & 0xff)


def words_to_int(words):
    if not valid_words(words):
        raise ValueError('%r is not a valid octet list for an IPv4 address!' % (words,))
    return _struct.unpack('>I', _struct.pack('4B', *words))[0]


def valid_bits(bits):
    return _valid_bits(bits, width, word_sep)


def bits_to_int(bits):
    return _bits_to_int(bits, width, word_sep)


def int_to_bits(int_val, word_sep=None):
    if word_sep is None:
        word_sep = globals()['word_sep']
    return _int_to_bits(int_val, word_size, num_words, word_sep)


def valid_bin(bin_val):
    return _valid_bin(bin_val, width)


def int_to_bin(int_val):
    return _int_to_bin(int_val, width)


def bin_to_int(bin_val):
    return _bin_to_int(bin_val, width)


def expand_partial_address(addr):
    tokens = []

    error = AddrFormatError("invalid partial IPv4 address: '{}'".format(addr))

    if isinstance(addr, str):
        if ':' in addr:
            #   Ignore IPv6 ...
            raise error

        try:
            if '.' in addr:
                tokens = ["{}".format(int(o)) for o in addr.split('.')]
            else:
                tokens = ["{}".format(int(addr))]
        except ValueError:
            raise error

        if 1 <= len(tokens) <= 4:
            for i in range(4 - len(tokens)):
                tokens.append('0')
        else:
            raise error

    if not tokens:
        raise error

    return "{}.{}.{}.{}".format(*tuple(tokens))

