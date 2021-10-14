import sys as _sys
from xml.sax import make_parser, handler

from netaddr.core import Publisher, Subscriber
from netaddr.ip import IPAddress, IPNetwork, IPRange, cidr_abbrev_to_verbose
from netaddr.compat import _dict_items, _callable, _importlib_resources

#: Topic based lookup dictionary for IANA information.
IANA_INFO = \
{
    'IPv4': {},
    'multicast': {},
}

class SaxRecordParser(handler.ContentHandler):
    def __init__(self, callback=None):
        self._level = 0
        self._is_active = False
        self._record = None
        self._tag_level = None
        self._tag_payload = None
        self._tag_feeding = None
        self._callback = callback

    def startElement(self, name, attrs):
        self._level += 1

        if self._is_active is False:
            if name == 'record':
                self._is_active = True
                self._tag_level = self._level
                self._record = {}
                if 'date' in attrs:
                    self._record['date'] = attrs['date']
        elif self._level == self._tag_level + 1:
            if name == 'xref':
                if 'type' in attrs and 'data' in attrs:
                    l = self._record.setdefault(attrs['type'], [])
                    l.append(attrs['data'])
            else:
                self._tag_payload = []
                self._tag_feeding = True
        else:
            self._tag_feeding = False

    def endElement(self, name):
        if self._is_active is True:
            if name == 'record' and self._tag_level == self._level:
                self._is_active = False
                self._tag_level = None
                if _callable(self._callback):
                    self._callback(self._record)
                self._record = None
            elif self._level == self._tag_level + 1:
                if name != 'xref':
                    self._record[name] = ''.join(self._tag_payload)
                    self._tag_payload = None
                    self._tag_feeding = False

        self._level -= 1

    def characters(self, content):
        if self._tag_feeding is True:
            self._tag_payload.append(content)

class XMLRecordParser(Publisher):
    def __init__(self, fh, **kwargs):
        super(XMLRecordParser, self).__init__()

        self.xmlparser = make_parser()
        self.xmlparser.setContentHandler(SaxRecordParser(self.consume_record))

        self.fh = fh

        self.__dict__.update(kwargs)

    def process_record(self, rec):
        return rec

    def consume_record(self, rec):
        record = self.process_record(rec)
        if record is not None:
            self.notify(record)

    def parse(self):
        self.xmlparser.parse(self.fh)

class IPv4Parser(XMLRecordParser):
    def __init__(self, fh, **kwargs):
        super(IPv4Parser, self).__init__(fh)

    def process_record(self, rec):
        record = {}
        for key in ('prefix', 'designation', 'date', 'whois', 'status'):
            record[key] = str(rec.get(key, '')).strip()

        #   Strip leading zeros from octet.
        if '/' in record['prefix']:
            (octet, prefix) = record['prefix'].split('/')
            record['prefix'] = '%d/%d' % (int(octet), int(prefix))

        record['status'] = record['status'].capitalize()

        return record

class MulticastParser(XMLRecordParser):
    def __init__(self, fh, **kwargs):
        super(MulticastParser, self).__init__(fh)

    def normalise_addr(self, addr):
        if '-' in addr:
            (a1, a2) = addr.split('-')
            o1 = a1.strip().split('.')
            o2 = a2.strip().split('.')
            return '%s-%s' % ('.'.join([str(int(i)) for i in o1]),
                              '.'.join([str(int(i)) for i in o2]))
        else:
            o1 = addr.strip().split('.')
            return '.'.join([str(int(i)) for i in o1])

    def process_record(self, rec):
        if 'addr' in rec:
            record = \
            {
                'address': self.normalise_addr(str(rec['addr'])),
                'descr': str(rec.get('description', '')),
            }
            return record

class DictUpdater(Subscriber):
    def __init__(self, dct, topic, unique_key):
        self.dct = dct
        self.topic = topic
        self.unique_key = unique_key

    def update(self, data):
        data_id = data[self.unique_key]

        if self.topic == 'IPv4':
            cidr = IPNetwork(cidr_abbrev_to_verbose(data_id))
            self.dct[cidr] = data
        elif self.topic == 'multicast':
            iprange = None
            if '-' in data_id:
                #   See if we can manage a single CIDR.
                (first, last) = data_id.split('-')
                iprange = IPRange(first, last)
                cidrs = iprange.cidrs()
                if len(cidrs) == 1:
                    iprange = cidrs[0]
            else:
                iprange = IPAddress(data_id)
            self.dct[iprange] = data

def load_info():
    ipv4 = IPv4Parser(_importlib_resources.open_binary(__package__, 'ipv4-address-space.xml'))
    ipv4.attach(DictUpdater(IANA_INFO['IPv4'], 'IPv4', 'prefix'))
    ipv4.parse()

    mcast = MulticastParser(_importlib_resources.open_binary(__package__, 'multicast-addresses.xml'))
    mcast.attach(DictUpdater(IANA_INFO['multicast'], 'multicast', 'address'))
    mcast.parse()

def pprint_info(fh=None):
    if fh is None:
        fh = _sys.stdout

    for category in sorted(IANA_INFO):
        fh.write('-' * len(category) + "\n")
        fh.write(category + "\n")
        fh.write('-' * len(category) + "\n")
        ipranges = IANA_INFO[category]
        for iprange in sorted(ipranges):
            details = ipranges[iprange]
            fh.write('%-45r' % (iprange) + details + "\n")

def _within_bounds(ip, ip_range):
    #   Boundary checking for multiple IP classes.
    if hasattr(ip_range, 'first'):
        #   IP network or IP range.
        return ip in ip_range
    elif hasattr(ip_range, 'value'):
        #   IP address.
        return ip == ip_range

    raise Exception('Unsupported IP range or address: %r!' % (ip_range,))

def query(ip_addr):
    info = {}
    if ip_addr.version == 4:
        for cidr, record in _dict_items(IANA_INFO['IPv4']):
            if _within_bounds(ip_addr, cidr):
                info.setdefault('IPv4', [])
                info['IPv4'].append(record)
        if ip_addr.is_multicast():
            for iprange, record in _dict_items(IANA_INFO['multicast']):
                if _within_bounds(ip_addr, iprange):
                    info.setdefault('Multicast', [])
                    info['Multicast'].append(record)
    return info

#   On module import, read IANA data files and populate lookups dict.
load_info()
