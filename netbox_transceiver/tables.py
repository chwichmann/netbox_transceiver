import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import TransceiverType, Transceiver, TransceiverTypeProfile

class TransceiverTypeTable(NetBoxTable):
    model = tables.Column(
        linkify=True,
        verbose_name='Transceiver Type'
    )
    manufacturer = tables.Column(
        linkify=True
    )
    instance_count = columns.LinkedCountColumn(
        viewname='plugins:netbox_transceiver:transceiver_list',
        url_params={'transceiver_type_id': 'pk'},
        verbose_name='Instances'
    )
    comments = columns.MarkdownColumn()
    tags = columns.TagColumn(
        url_name='plugins:netbox_transceiver:transceiver_list'
    )

    class Meta(NetBoxTable.Meta):
        model = TransceiverType
        fields = ('pk', 'id', 'model', 'manufacturer', 'part_number', 'physic', 'form',
                 'profiles', 'tx_power_min', 'tx_power_max', 'rx_power_min', 'rx_power_max')
        default_columns = ('pk', 'model', 'manufacturer', 'part_number', 'physic', 'form')

class TransceiverTypeProfileTable(NetBoxTable):
    profile = tables.Column(
        linkify=True,
        )
    group = tables.Column()
    type_count = columns.LinkedCountColumn(
        viewname='plugins:netbox_transceiver:transceivertype_list',
        url_params={'profiles_id': 'pk'},
        verbose_name='Types'
    )
    transceiver_count = columns.LinkedCountColumn(
        viewname='plugins:netbox_transceiver:transceiver_list',
        url_params={'transceiver_id': 'pk'},
        verbose_name='Transceivers'
    )

    class Meta(NetBoxTable.Meta):
        model = TransceiverTypeProfile
        fields = ('profile', 'group', 'type_count', 'transceiver_count')
        default_columns = ('profile', 'group', 'type_count', 'transceiver_count')


class TransceiverTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
    )
    device = tables.Column(
        linkify=True
    )
    interface = tables.Column(
        linkify=True
    )
    manufacturer = tables.Column(
        accessor=tables.A('transceiver_type__manufacturer'),
        linkify=True
    )
    transceiver_type = tables.Column(
        linkify=True
    )
    status = columns.ChoiceFieldColumn()
    tags = columns.TagColumn(
        url_name='plugins:netbox_transceiver:transceiver_list'
    )

    class Meta(NetBoxTable.Meta):
        model = Transceiver
        fields = (
            'pk', 'id', 'name', 'device', 'interface', 'manufacturer', 'transceiver_type', 'profile', 'status', 'serial', 'asset_tag',
            'description', 'tags',
        )
        default_columns = (
            'name', 'transceiver_type', 'profile', 'status'
        )
