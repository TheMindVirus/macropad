import os
import sys
import ciscopad.netaddr as netaddr

#   aliases to save some typing ...
from ciscopad.netaddr import IPAddress as IP, IPNetwork as CIDR
from ciscopad.netaddr import EUI as MAC

def main():
    argv = sys.argv[1:]

    banner = "\nnetaddr shell {} - {}\n".format(netaddr.__version__, __doc__)
    exit_msg = "\nShare and enjoy!"
    rc_override = None

    try:
        try:
            # ipython >= 0.11
            from IPython.terminal.embed import InteractiveShellEmbed
            ipshell = InteractiveShellEmbed(banner1=banner, exit_msg=exit_msg)
        except ImportError:
            # ipython < 0.11
            from IPython.Shell import IPShellEmbed
            ipshell = IPShellEmbed(argv, banner, exit_msg, rc_override)
    except ImportError:
        sys.stderr.write('IPython (http://ipython.scipy.org/) not found!\n')
        sys.exit(1)
    ipshell()

if __name__ == '__main__':
    main()
