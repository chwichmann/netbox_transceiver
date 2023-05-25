from netbox.api.viewsets import NetBoxModelViewSet
from utilities.utils import count_related

from .. import filtersets, models
from ..models import Transceiver, TransceiverType
from .serializers import TransceiverTypeSerializer, TransceiverTypeProfileSerializer, TransceiverSerializer

class TransceiverTypeViewSet(NetBoxModelViewSet):
    queryset = models.TransceiverType.objects.prefetch_related('tags').annotate(
        transceiver_count=count_related(Transceiver, 'transceiver_type')
        )
    serializer_class = TransceiverTypeSerializer

class TransceiverTypeProfileViewSet(NetBoxModelViewSet):
    queryset = models.TransceiverTypeProfile.objects.prefetch_related('group').annotate(
        instance_count=count_related(TransceiverType, 'profiles')
        )
    serializer_class = TransceiverTypeProfileSerializer

class TransceiverViewSet(NetBoxModelViewSet):
    queryset = models.Transceiver.objects.prefetch_related('tags')
    serializer_class = TransceiverSerializer
