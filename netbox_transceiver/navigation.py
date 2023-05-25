from extras.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_transceiver:transceiver_list",
        link_text="Transceivers",
    ),

    PluginMenuItem(
        link="plugins:netbox_transceiver:transceivertype_list",
        link_text="Transceiver Types",
    ),

    PluginMenuItem(
        link="plugins:netbox_transceiver:transceivertypeprofile_list",
        link_text="Transceiver Profiles",
    ),
)
