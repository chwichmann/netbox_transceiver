from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import TransceiverType, Transceiver
from .nested_serializers import *

class TransceiverTypeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_transceiver-api:transceivertype-detail'
    )

    class Meta:
        model = TransceiverType
        fields = (
            'id', 'url', 'model', 'manufacturer', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
            )

class TransceiverSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_transceiver-api:transceiver-detail'
    )

    class Meta:
        model = Transceiver
        fields = (
            'id', 'url', 'device', 'model', 'interface', 'transceiver_type', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
            )