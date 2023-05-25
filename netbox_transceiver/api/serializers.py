from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import TransceiverType, TransceiverTypeProfile, Transceiver

class TransceiverTypeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_transceiver-api:transceivertype-detail'
    )

    class Meta:
        model = TransceiverType
        fields = (
            'id', 'url', 'model', 'manufacturer', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
            )

class TransceiverTypeProfileSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_transceiver-api:transceivertypeprofile-detail'
    )

    class Meta:
        model = TransceiverTypeProfile
        fields = (
            'id', 'url', 'profile', 'group',
            )


class TransceiverSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_transceiver-api:transceiver-detail'
    )

    class Meta:
        model = Transceiver
        fields = (
            'id', 'url', 'device', 'interface', 'transceiver_type', 'tags', 'custom_fields', 'created', 'last_updated',
            )