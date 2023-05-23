from netbox.views import generic
from .models import Transceiver, TransceiverType
from . import forms, tables, filtersets
from utilities.utils import count_related

# TransceiverType
class TransceiverTypeView(generic.ObjectView):
    queryset = TransceiverType.objects.all()

    def get_extra_context(self, request, instance):
        related_models = (
            (Transceiver.objects.restrict(request.user).filter(transceiver_type=instance), 'transceiver_type_id'),
        )

        return {
            'related_models': related_models,
        }

class TransceiverTypeListView(generic.ObjectView):
    queryset = TransceiverType.objects.annotate(
        instance_count=count_related(Transceiver, 'transceiver_type')
        )
    filterset = filtersets.TransceiverTypeFilterSet
    filterset_form = forms.TransceiverTypeFilterForm
    table = tables.TransceiverTypeTable

class TransceiverTypeEditView(generic.ObjectEditView):
    queryset = TransceiverType.objects.all()
    form = forms.TransceiverTypeForm

class TransceiverTypeBulkDeleteView(generic.BulkDeleteView):
    queryset = TransceiverType.objects.all()
    table = tables.TransceiverTypeTable

class TransceiverTypeBulkEditView(generic.BulkEditView):
    queryset = TransceiverType.objects.all()
    filterset = filters.TransceiverTypeFilterSet
    table = tables.TransceiverTypeTable
    form = forms.TransceiverTypeForm

class TransceiverTypeDeleteView(generic.ObjectDeleteView):
    queryset = TransceiverType.objects.all()

# Transceiver
class TransceiverView(generic.ObjectView):
    queryset = Transceiver.objects.all()

class TransceiverListView(generic.ObjectView):
    queryset = Transceiver.objects.all()
    table = tables.TransceiverTable

class TransceiverEditView(generic.ObjectEditView):
    queryset = Transceiver.objects.all()
    form = forms.TransceiverForm

class TransceiverBulkDeleteView(generic.BulkDeleteView):
    queryset = Transceiver.objects.all()
    table = tables.TransceiverTable

class TransceiverBulkEditView(generic.BulkEditView):
    queryset = Transceiver.objects.all()
    filterset = filters.TransceiverFilterSet
    table = tables.TransceiverTable
    form = forms.TransceiverForm

class TransceiverDeleteView(generic.ObjectDeleteView):
    queryset = Transceiver.objects.all()