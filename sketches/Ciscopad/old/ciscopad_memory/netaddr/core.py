import sys as _sys
import ciscopad.lib._collections_abc #Avoids import chain of length >10
import ciscopad.lib.pprint as _pprint

#: True if platform is natively big endian, False otherwise.
BIG_ENDIAN_PLATFORM = _sys.byteorder == 'big'

#:  Use inet_pton() semantics instead of inet_aton() when parsing IPv4.
P = INET_PTON = 1

#:  Remove any preceding zeros from IPv4 address octets before parsing.
Z = ZEROFILL = 2

#:  Remove any host bits found to the right of an applied CIDR prefix.
N = NOHOST = 4

#-----------------------------------------------------------------------------
#   Custom exceptions.
#-----------------------------------------------------------------------------
class AddrFormatError(Exception):
    pass

class AddrConversionError(Exception):
    pass

class NotRegisteredError(Exception):
    pass

try:
    a = 42
    a.bit_length()
    # No exception, must be Python 2.7 or 3.1+ -> can use bit_length()
    def num_bits(int_val):
        return int_val.bit_length()
except AttributeError:
    # a.bit_length() excepted, must be an older Python version.
    def num_bits(int_val):
        numbits = 0
        while int_val:
            numbits += 1
            int_val >>= 1
        return numbits

class Subscriber(object):
    def update(self, data):
        raise NotImplementedError('cannot invoke virtual method!')

class PrettyPrinter(Subscriber):
    def __init__(self, fh=_sys.stdout, write_eol=True):
        self.fh = fh
        self.write_eol = write_eol

    def update(self, data):
        self.fh.write(_pprint.pformat(data))
        if self.write_eol:
            self.fh.write("\n")

class Publisher(object):
    def __init__(self):
        self.subscribers = []

    def attach(self, subscriber):
        if hasattr(subscriber, 'update') and _callable(eval('subscriber.update')):
            if subscriber not in self.subscribers:
                self.subscribers.append(subscriber)
        else:
            raise TypeError('%r does not support required interface!' % subscriber)

    def detach(self, subscriber):
        try:
            self.subscribers.remove(subscriber)
        except ValueError:
            pass

    def notify(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)

class DictDotLookup(object):
    def __init__(self, d):
        for k in d:
            if isinstance(d[k], dict):
                self.__dict__[k] = DictDotLookup(d[k])
            elif isinstance(d[k], (list, tuple)):
                l = []
                for v in d[k]:
                    if isinstance(v, dict):
                        l.append(DictDotLookup(v))
                    else:
                        l.append(v)
                self.__dict__[k] = l
            else:
                self.__dict__[k] = d[k]

    def __getitem__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]

    def __iter__(self):
        return _iter_dict_keys(self.__dict__)

    def __repr__(self):
        return _pprint.pformat(self.__dict__)
