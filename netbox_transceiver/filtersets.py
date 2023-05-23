import django_filters
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet
from .models import *
from .choices import *
from dcim.models.devices import Manufacturer, Device

from utilities.filters import MultiValueCharFilter

class TransceiverTypeFilterSet(NetBoxModelFilterSet):
    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Manufacturer.objects.all(),
        label=_('Manufacturer (ID)'),
    )
    manufacturer = django_filters.ModelMultipleChoiceFilter(
        field_name='manufacturer__slug',
        queryset=Manufacturer.objects.all(),
        to_field_name='slug',
        label=_('Manufacturer (slug)'),
    )

    class Meta:
        model = TransceiverType
        fields = ['id', 'model', 'part_number']


class TransceiverFilterSet(NetBoxModelFilterSet):
    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        field_name='transceiver_type__manufacturer',
        queryset=Manufacturer.objects.all(),
        label=_('Manufacturer (ID)'),
    )
    manufacturer = django_filters.ModelMultipleChoiceFilter(
        field_name='transceiver_type__manufacturer__slug',
        queryset=Manufacturer.objects.all(),
        to_field_name='slug',
        label=_('Manufacturer (slug)'),
    )
    device_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        label=_('Device (ID)'),
    )
    transceiver_type = django_filters.ModelMultipleChoiceFilter(
        field_name='transceiver_type__model',
        queryset=TransceiverType.objects.all(),
        to_field_name='model',
        label=_('Transceiver type (model)'),
    )
    transceiver_type_id = django_filters.ModelMultipleChoiceFilter(
        queryset=TransceiverType.objects.all(),
        label=_('Transceiver type (ID)'),
    )
    status = django_filters.MultipleChoiceFilter(
        choices=TransceiverStatusChoices,
        null_value=None
    )
    serial = MultiValueCharFilter(
        lookup_expr='iexact'
    )

    class Meta:
        model = Transceiver
        fields = ['id', 'status', 'asset_tag']

