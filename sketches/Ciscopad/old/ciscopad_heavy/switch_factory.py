from ciscopad.cisco import cisco_core
from ciscopad.cisco6500 import cisco_core as cisco6500_core

DEFAULT_MAPPING = \
{
    'cisco_generic': cisco_core.CiscoSwitchCore,
    'cisco_6500': cisco6500_core.Cisco6500SwitchCore,
}

class SwitchFactory(object):
    def __init__(self, mapping=None):
        if mapping is None:
            mapping = DEFAULT_MAPPING
        self.mapping = mapping

    def get(self, switch_model, hostname='switch_hostname', password='root', ports=None, **kwargs):
        try:
            core = self.mapping[switch_model]
        except KeyError:
            raise InvalidSwitchModel(switch_model)

        return core(
            switch_configuration.SwitchConfiguration(
                '127.0.0.1',
                name=hostname,
                privileged_passwords=[password],
                ports=ports or core.get_default_ports(),
                **kwargs
            )
        )

class SwitchFactoryException(Exception):
    pass

class InvalidSwitchModel(SwitchFactoryException):
    pass
