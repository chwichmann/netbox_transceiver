from netbox.api.routers import NetBoxRouter
from .views import *

router = NetBoxRouter()
router.register('transceivertype', TransceiverTypeViewSet)
router.register('transceiver', TransceiverViewSet)
urlpatterns = router.urls