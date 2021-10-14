#: Version info (major, minor, maintenance, status)
__version__ = '0.8.0'
VERSION = tuple(int(part) for part in __version__.split('.'))
STATUS = ''

import sys as _sys

from ciscopad.netaddr.ip import IPNetwork
#import ciscopad.netaddr.ip.core as ip
#import ciscopad.netaddr.ip.sets as sets
#import ciscopad.netaddr.ip.glob as glob
#import ciscopad.netaddr.ip.nmap as nmap