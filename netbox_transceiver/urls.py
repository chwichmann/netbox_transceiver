from django.urls import include, path

from . import views
from utilities.urls import get_model_urls

app_name = "netbox_transceiver"

urlpatterns = [

    # TransceiverTypes
    path('transceivertype/', views.TransceiverTypeListView.as_view(), name='transceivertype_list'),
    path('transceivertype/add/', views.TransceiverTypeEditView.as_view(), name='transceivertype_add'),
    path('transceivertype/delete/', views.TransceiverTypeBulkDeleteView.as_view(), name='transceivertype_bulk_delete'),
    path('transceivertype/edit/', views.TransceiverTypeBulkEditView.as_view(), name='transceivertype_bulk_edit'),
    path('transceivertype/<int:pk>/', include(get_model_urls('netbox_transceiver', 'transceivertype'))),

    # Transceiver
    path('transceiver/', views.TransceiverListView.as_view(), name='transceiver_list'),
    path('transceiver/add/', views.TransceiverEditView.as_view(), name='transceiver_add'),
    path('transceiver/delete/', views.TransceiverBulkDeleteView.as_view(), name='transceiver_bulk_delete'),
    path('transceiver/edit/', views.TransceiverBulkEditView.as_view(), name='transceiver_bulk_edit'),
    path('transceiver/<int:pk>/', include(get_model_urls('netbox_transceiver', 'transceiver'))),

]