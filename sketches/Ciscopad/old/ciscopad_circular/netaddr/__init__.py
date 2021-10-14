#: Version info (major, minor, maintenance, status)
__version__ = '0.8.0'
VERSION = tuple(int(part) for part in __version__.split('.'))
STATUS = ''

import sys as _sys

from ciscopad.netaddr.core import (AddrConversionError, AddrFormatError,
    NotRegisteredError, ZEROFILL, Z, INET_PTON, P, NOHOST, N)
"""
from ciscopad.netaddr.ip import (IPAddress, IPNetwork, IPRange, all_matching_cidrs,
    cidr_abbrev_to_verbose, cidr_exclude, cidr_merge, iprange_to_cidrs,
    iter_iprange, iter_unique_ips, largest_matching_cidr,
    smallest_matching_cidr, spanning_cidr)
"""
import ciscopad.netaddr.ip

from ciscopad.netaddr.ip.sets import IPSet

from ciscopad.netaddr.ip.glob import (IPGlob, cidr_to_glob, glob_to_cidrs,
    glob_to_iprange, glob_to_iptuple, iprange_to_globs, valid_glob)

from ciscopad.netaddr.ip.nmap import valid_nmap_range, iter_nmap_range

from ciscopad.netaddr.strategy.ipv4 import valid_str as valid_ipv4

from ciscopad.netaddr.contrib.subnet_splitter import SubnetSplitter
