from extras.plugins import PluginConfig

class NetboxTransceiverConfig(PluginConfig):
    name = 'netbox_transceiver'
    verbose_name = ' Netbox Transceiver'
    description = 'Adds transceivers to your network'
    version = '0.1'
    author = 'Christian Wichmann'
    author_email = 'christian.wichmann@outlook.com'
    base_url = 'transceiver'
    required_settings = []
    default_settings = {}

config = NetboxTransceiverConfig