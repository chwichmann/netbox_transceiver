from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import *
from dcim.models import Manufacturer, Device, Module, Interface

class TransceiverTypeForm(NetBoxModelForm):
    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all()
    )
    comments = CommentField()

    fieldsets = (
        ('Transceiver type', ('model', 'manufacturer', 'part_number', 'tags')),
        ('Specifications', ('physic', 'form', 'profile', 'tx_power_min',
                           'tx_power_max', 'rx_power_min', 'rx_power_max')),
    )

    class Meta:
        model = TransceiverType
        fields = ('model', 'manufacturer', 'part_number', 'comments', 'tags', 
                  'physic', 'form', 'profile', 'tx_power_min', 'tx_power_max', 
                  'rx_power_min', 'rx_power_max')

class TransceiverForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        initial_params={
            'device_id': '$device'
        }
    )
    module = DynamicModelChoiceField(
        queryset=Module.objects.all(),
        initial_params={
            'module_id': '$module'
        },
        query_params={
            'device_id': '$device'
        }
    )
    interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        initial_params={
            'interface_id': '$interface'
        },
        query_params={
            'module_id': '$module'
        }
    )
    transceiver_type = DynamicModelChoiceField(
        queryset=Transceiver.objects.all(),
        selector=True
    )

    fieldsets = (
        ('Transceiver', ('device', 'module', 'transceiver_type', 'status', 'description', 'tags')),
        ('Hardware', (
            'serial', 'asset_tag' )),
    )
