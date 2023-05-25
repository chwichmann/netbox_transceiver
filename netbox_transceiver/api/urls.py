from netbox.api.routers import NetBoxRouter

from .views import TransceiverTypeProfileViewSet, TransceiverTypeViewSet, TransceiverViewSet

router = NetBoxRouter()
router.register('transceivertypeprofile', TransceiverTypeProfileViewSet)
router.register('transceivertype', TransceiverTypeViewSet)
router.register('transceiver', TransceiverViewSet)

app_name='netbox_transceiver-api'
urlpatterns = router.urls