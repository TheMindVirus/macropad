import re
from ciscopad.lib.functools import partial

from ciscopad import group_sequences
from ciscopad.command_processing.base_command_processor import BaseCommandProcessor
from ciscopad.switch_configuration import VlanPort, AggregatedPort

class EnabledCommandProcessor(BaseCommandProcessor):
    def __init__(self, config):
        super(EnabledCommandProcessor, self).__init__()
        self.config_processor = config

    def get_prompt(self):
        return self.switch_configuration.name + "#"

    def do_enable(self, *args):
        pass

    def do_configure(self, *_):
        self.write_line("Enter configuration commands, one per line.  End with CNTL/Z.")
        self.move_to(self.config_processor)

    def do_show(self, *args):
        if "running-config".startswith(args[0]):
            if len(args) < 2:
                self.show_run()
            elif "vlan".startswith(args[1]):
                self.write_line("Building configuration...")
                self.write_line("")
                self.write_line("Current configuration:")
                for vlan in self.switch_configuration.vlans:
                    if vlan.number == int(args[2]):
                        self.write_line("\n".join(["!"] + build_running_vlan(vlan)))
                self.write_line("end")
                self.write_line("")
            elif "interface".startswith(args[1]):
                if_name = "".join(args[2:])
                port = self.switch_configuration.get_port_by_partial_name(if_name)

                if port:
                    self.write_line("Building configuration...")
                    self.write_line("")

                    data = ["!"] + build_running_interface(port) + ["end", ""]

                    self.write_line("Current configuration : %i bytes" % (len("\n".join(data)) + 1))
                    [self.write_line(l) for l in data]
                else:
                    self.write_line("                               ^")
                    self.write_line("% Invalid input detected at '^' marker.")
                    self.write_line("")

        elif "vlan".startswith(args[0]):
            self.write_line("")
            self.write_line("VLAN Name                             Status    Ports")
            self.write_line("---- -------------------------------- --------- -------------------------------")
            for vlan in sorted(self.switch_configuration.vlans, key=lambda v: v.number):
                ports = [port.get_subname(length=2) for port in self.switch_configuration.get_physical_ports()
                         if port.access_vlan == vlan.number or (vlan.number == 1 and port.access_vlan is None)]
                formatted_membership = []
                if ports:
                    ports_membership = ["    {}".format(l) for l in get_port_groups(ports, max_line_length=30)]
                    formatted_membership.append(ports_membership.pop(0))
                    for remaining_line in ports_membership:
                        formatted_membership.append(' ' * 44 + remaining_line)

                self.write_line("%-4s %-32s %s%s" % (
                    vlan.number,
                    vlan_display_name(vlan),
                    "active",
                    '\n'.join(formatted_membership)
                ))
            if len(args) == 1:
                self.write_line("")
                self.write_line("VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2")
                self.write_line("---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------")
                for vlan in sorted(self.switch_configuration.vlans, key=lambda v: v.number):
                    self.write_line("%-4s enet  10%04d     1500  -      -      -        -    -        0      0" % (vlan.number, vlan.number))
                self.write_line("")
                self.write_line("Remote SPAN VLANs")
                self.write_line("------------------------------------------------------------------------------")
                self.write_line("")
                self.write_line("")
                self.write_line("Primary Secondary Type              Ports")
                self.write_line("------- --------- ----------------- ------------------------------------------")
                self.write_line("")
        elif "etherchannel".startswith(args[0]) and len(args) == 2 and "summary".startswith(args[1]):
            ports = sorted(self.switch_configuration.ports, key=lambda x: x.name)
            port_channels = sorted(
                [p for p in ports if isinstance(p, AggregatedPort)],
                key=port_channel_number)
            self.write_line("Flags:  D - down        P - bundled in port-channel")
            self.write_line("        I - stand-alone s - suspended")
            self.write_line("        H - Hot-standby (LACP only)")
            self.write_line("        R - Layer3      S - Layer2")
            self.write_line("        U - in use      f - failed to allocate aggregator")
            self.write_line("")
            self.write_line("        M - not in use, minimum links not met")
            self.write_line("        u - unsuitable for bundling")
            self.write_line("        w - waiting to be aggregated")
            self.write_line("        d - default port")
            self.write_line("")
            self.write_line("")
            self.write_line("Number of channel-groups in use: {}".format(len(port_channels)))
            self.write_line("Number of aggregators:           {}".format(len(port_channels)))
            self.write_line("")
            self.write_line("Group  Port-channel  Protocol    Ports")
            self.write_line("------+-------------+-----------+-----------------------------------------------")
            for port_channel in port_channels:
                members = [short_name(p) for p in ports
                           if p.aggregation_membership == port_channel.name]
                self.write_line(
                    "{: <6} {: <13} {: <11} {}".format(
                        port_channel_number(port_channel),
                        "{}(S{})".format(short_name(port_channel), "U" if members else ""),
                        "  LACP",
                        "  ".join("{}(P)".format(m) for m in members)))
            self.write_line("")
        elif "ip".startswith(args[0]):
            if "interface".startswith(args[1]):
                if_list = None
                if len(args) > 2:
                    interface = self.switch_configuration.get_port_by_partial_name("".join(args[2:]))
                    if interface:
                        if_list = [interface]
                    else:
                        self.write_line("                                 ^")
                        self.write_line("% Invalid input detected at '^' marker.")
                        self.write_line("")
                else:
                    if_list = self.switch_configuration.get_vlan_ports() + self.switch_configuration.get_physical_ports()
                if if_list:
                    for interface in if_list:
                        self.write_line("{} is down, line protocol is down".format(interface.name))
                        if not isinstance(interface, VlanPort):
                            self.write_line("  Internet protocol processing disabled")
                        else:
                            if len(interface.ips) == 0:
                                self.write_line("  Internet protocol processing disabled")
                            else:
                                self.write_line("  Internet address is {}".format(interface.ips[0]))
                                for ip in interface.ips[1:]:
                                    self.write_line("  Secondary address {}".format(ip))
                                self.write_line("  Outgoing access list is {}".format(interface.access_group_out if interface.access_group_out else "not set"))
                                self.write_line("  Inbound  access list is {}".format(interface.access_group_in if interface.access_group_in else "not set"))
                                if interface.vrf is not None:
                                    self.write_line("  VPN Routing/Forwarding \"{}\"".format(interface.vrf.name))
            elif "route".startswith(args[1]):
                if "static".startswith(args[2]):
                    routes = self.switch_configuration.static_routes
                    for route in routes:
                        self.write_line("S        {0} [x/y] via {1}".format(route.destination, route.next_hop))
                self.write_line("")
        elif "version".startswith(args[0]):
            self.show_version()

    def do_copy(self, source_url, destination_url):
        dest_protocol, dest_file = destination_url.split(":")
        self.write("Destination filename [{}]? ".format(strip_leading_slash(dest_file)))
        self.continue_to(partial(self.continue_validate_copy, source_url))

    def continue_validate_copy(self, source_url, _):
        self.write_line("Accessing {}...".format(source_url))
        try:
            url, filename = re.match('tftp://([^/]*)/(.*)', source_url).group(1, 2)
            SwitchTftpParser(self.switch_configuration).parse(url, filename, self.config_processor)
            self.write_line("Done (or some official message...)")
        except Exception as e:
            self.logger.warning("tftp parsing went wrong : %s" % str(e))
            self.write_line("Error opening %s (Timed out)" % source_url)

    def do_terminal(self, *args):
        pass

    def do_write(self, *args):
        self.write_line("Building configuration...")
        self.switch_configuration.commit()
        self.write_line("OK")

    def do_exit(self):
        self.is_done = True

    def show_run(self):

        all_data = [
            "version 12.1",
            "!",
            "hostname {}".format(self.switch_configuration.name),
            "!",
            "!",
        ]
        for vlan in self.switch_configuration.vlans:
            all_data = all_data + build_running_vlan(vlan) + ["!"]
        for interface in self.switch_configuration.get_physical_ports() + self.switch_configuration.get_vlan_ports():
            all_data = all_data + build_running_interface(interface) + ["!"]
        if self.switch_configuration.static_routes:
            for route in self.switch_configuration.static_routes:
                all_data.append(build_static_routes(route))
            all_data.append("!")

        all_data += ["end", ""]

        self.write_line("Building configuration...")
        self.write_line("")

        self.write_line("Current configuration : {} bytes".format(len("\n".join(all_data)) + 1))
        [self.write_line(l) for l in all_data]

    def show_version(self):
        self.write_line(version_text(
            hostname=self.switch_configuration.name,
            vlan_port_count=len(self.switch_configuration.get_vlan_ports()),
            port_count=len(self.switch_configuration.get_physical_ports()),
        ))

###

def version_text(**kwargs):
    return """
Cisco IOS Software, C3750 Software (CP7-IPSERVICES-K-9), Version 3.4.0(58)SE2, DEBUG SOFTWARE
(V) 2021 by Cisco Systems, Inc.
Compiled Thu 14-Oct-21 06:11 by The

ROM: Bootstrap program is CP7 boot loader
BOOTLDR: CP7 Boot Loader (CP7-HBOOT-M) Version 3.4.0(44)FC1, DEBUG SOFTWARE

{hostname} uptime is 9 years, 9 weeks, 9 days, 9 hours, 9 minutes
System returned to ROM by power-on
System image file is "flash:cp7-ipservices-k-9-mz.122-58.SE2.bin"

{hostname} WS-CP7-24TS-1U (RP2040) processor (revision RP2) with 264K bytes of memory.
Processor board ID FOC1530X2F7
Last reset from power-on
{vlan_port_count} Virtual Ethernet interfaces
{port_count} Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

256K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 00:00:00:00:00:00
Motherboard assembly number     : 73-10219-09
Power supply part number        : 341-0098-02
Motherboard serial number       : FOC153019Z6
Power supply serial number      : ALD153000BB
Model revision number           : RP2
Motherboard revision number     : M0
Model number                    : WS-CP7-24TS-S1U
System serial number            : FOC1530X2F7
Top Assembly Part Number        : 800-26859-03
Top Assembly Revision Number    : C0
Version ID                      : V05
CLEI Code Number                : COMB600BRA
Hardware Board Revision Number  : 0x09

Switch Ports Model              SW Version            SW Image
------ ----- -----              ----------            ----------
*    1 {port_count: <5} WS-CP7-24TS-1U  12.2(58)SE2           CP7-IPSERVICES-K-9
""".format(**kwargs)[1:]
