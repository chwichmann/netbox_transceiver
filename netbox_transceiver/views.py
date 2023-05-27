from netbox.views import generic
from .models import *
from . import forms, tables, filtersets
from utilities.utils import count_related

# TransceiverType
class TransceiverTypeView(generic.ObjectView):
    queryset = TransceiverType.objects.all()

    def get_extra_context(self, request, instance):
        related_transceiver = (
            (Transceiver.objects.restrict(request.user).filter(transceiver_type=instance), 'transceiver_type_id'),
        )

        return {
            'related_transceiver': related_transceiver,
        }

class TransceiverTypeListView(generic.ObjectListView):
    queryset = TransceiverType.objects.annotate(
        instance_count=count_related(Transceiver, 'transceiver_type'),
        )
    filterset = filtersets.TransceiverTypeFilterSet
    #filterset_form = forms.TransceiverTypeFilterForm
    table = tables.TransceiverTypeTable


class TransceiverTypeEditView(generic.ObjectEditView):
    queryset = TransceiverType.objects.all()
    form = forms.TransceiverTypeForm

    #def get_extra_context(self, request, instance):
    #    profiles = TransceiverTypeProfile.objects.filter(profile=instance)

    #    return {
    #        'profiles': profiles,
    #        }


class TransceiverTypeBulkDeleteView(generic.BulkDeleteView):
    queryset = TransceiverType.objects.all()
    table = tables.TransceiverTypeTable

class TransceiverTypeBulkEditView(generic.BulkEditView):
    queryset = TransceiverType.objects.all()
    #filterset = filtersets.TransceiverTypeFilterSet
    table = tables.TransceiverTypeTable
    form = forms.TransceiverTypeForm

class TransceiverTypeDeleteView(generic.ObjectDeleteView):
    queryset = TransceiverType.objects.all()

# TransceiverTypeProfile
class TransceiverTypeProfileListView(generic.ObjectListView):
    queryset = TransceiverTypeProfile.objects.annotate(
        type_count=count_related(TransceiverType, 'profiles'),
        transceiver_count=count_related(Transceiver, 'profile'),
        )
    table = tables.TransceiverTypeProfileTable

class TransceiverTypeProfileView(generic.ObjectView):
    queryset = TransceiverTypeProfile.objects.all()

class TransceiverTypeProfileEditView(generic.ObjectEditView):
    queryset = TransceiverTypeProfile.objects.all()
    form = forms.TransceiverTypeProfileForm

class TransceiverTypeProfileBulkDeleteView(generic.BulkDeleteView):
    queryset = TransceiverTypeProfile.objects.all()
    table = tables.TransceiverTypeProfileTable

class TransceiverTypeProfileBulkEditView(generic.BulkEditView):
    queryset = TransceiverTypeProfile.objects.all()
    #filterset = filters.TransceiverFilterSet
    table = tables.TransceiverTypeProfileTable
    form = forms.TransceiverTypeProfileForm

class TransceiverTypeProfileDeleteView(generic.ObjectDeleteView):
    queryset = Transceiver.objects.all()

# Transceiver
class TransceiverView(generic.ObjectView):
    queryset = Transceiver.objects.all()

class TransceiverListView(generic.ObjectListView):
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
    #filterset = filters.TransceiverFilterSet
    table = tables.TransceiverTable
    form = forms.TransceiverForm

class TransceiverDeleteView(generic.ObjectDeleteView):
    queryset = Transceiver.objects.all()