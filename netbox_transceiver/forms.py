from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
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
        ('Specifications', ('physic', 'form', 'profiles', 'tx_power_min', 'tx_power_max',
                           'rx_power_min', 'rx_power_max', 'power_budget')),
    )

    class Meta:
        model = TransceiverType
        fields = ('model', 'manufacturer', 'part_number', 'comments', 'tags', 
                  'physic', 'form', 'profiles', 'tx_power_min', 'tx_power_max',
                 'rx_power_min', 'rx_power_max')

class TransceiverTypeProfileForm(NetBoxModelForm):

    fieldsets = (
        ('Profile', ('profile', 'group')),
    )

    class Meta:
        model = TransceiverTypeProfile
        fields = ('profile', 'group')

class TransceiverForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        initial_params={
            'id': '$device'
        }
    )
    interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        initial_params={
            'id': '$interface'
        },
        query_params={
            'device_id': '$device'
        }
    )
   
    fieldsets = (
        ('Transceiver', ('device', 'interface', 'transceiver_type', 'profile', 'status', 'description', 'tags')),
        ('Hardware', (
            'serial', 'asset_tag' )),
    )

    class Meta:
        model = Transceiver
        fields = ('device', 'interface','transceiver_type', 'profile', 'status', 'description', 'serial', 'asset_tag')

class TransceiverTypelFilterForm(NetBoxModelFilterSetForm):
    model = TransceiverType

    fieldsets = (
        (None, ('q', 'filter_id', 'tag')),
        ('Hardware', ('manufacturer_id', 'part_number')),
        ('Specifications', (
            'physic', 'form', 'rx_power_min', 'rx_power_max', 'tx_power_min',
            'tx_power_max',
        )),
        ('Weight', ('weight', 'weight_unit')),
    )
