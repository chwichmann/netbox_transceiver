from netbox.api.viewsets import NetBoxModelViewSet
from utilities.utils import count_related

from .. import filtersets, models
from .serializers import *

class TransceiverTypeViewSet(NetBoxModelViewSet):
    queryset = models.TransceiverType.objects.prefetch_related('tags').annotate(
        transceiver_count=count_related(Transceiver, 'transceiver_type')
        )
    serializer_class = TransceiverTypeSerializer

class TransceiverViewSet(NetBoxModelViewSet):
    queryset = models.Transceiver.objects.prefetch_related('tags')
    serializer_class = TransceiverSerializer
