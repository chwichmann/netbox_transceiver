import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import *

class TransceiverTypeTable(NetBoxTable):
    model = tables.Column(
        linkify=True,
        verbose_name='Transceiver Type'
    )
    manufacturer = tables.Column(
        linkify=True
    )
    instance_count = columns.LinkedCountColumn(
        viewname='dcim:transceiver_list',
        url_params={'transceiver_type_id': 'pk'},
        verbose_name='Instances'
    )
    comments = columns.MarkdownColumn()
    tags = columns.TagColumn(
        url_name='dcim:moduletype_list'
    )

    class Meta(NetBoxTable.Meta):
        model = TransceiverType
        fields = ('pk', 'id', 'model', 'manufacturer', 'part_number', 'physic', 'form',
                 'profile', 'tx_power_min', 'tx_power_max', 'rx_power_min', 'rx_power_max')
        default_columns = ('pk', 'model', 'manufacturer', 'part_number', 'physic', 'form')

class TransceiverTable(NetBoxTable):
    device = tables.Column(
        linkify=True
    )
    module = tables.Column(
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
    comments = columns.MarkdownColumn()
    tags = columns.TagColumn(
        url_name='dcim:transceiver_list'
    )

    class Meta(NetBoxTable.Meta):
        model = Transceiver
        fields = (
            'pk', 'id', 'device', 'module', 'interface', 'manufacturer', 'transceiver_type', 'status', 'serial', 'asset_tag',
            'description', 'comments', 'tags',
        )
        default_columns = (
            'pk', 'id', 'device', 'module', 'interface', 'transceiver_type', 'status'
        )
