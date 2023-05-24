from django.urls import  path

from . import models, views
from netbox.views.generic import ObjectChangeLogView

app_name = "transceiver"

urlpatterns = (

    # TransceiverTypes
    path('transceivertype/', views.TransceiverTypeListView.as_view(), name='transceivertype_list'),
    path('transceivertype/add/', views.TransceiverTypeEditView.as_view(), name='transceivertype_add'),
    path('transceivertype/delete/', views.TransceiverTypeBulkDeleteView.as_view(), name='transceivertype_bulk_delete'),
    path('transceivertype/edit/', views.TransceiverTypeBulkEditView.as_view(), name='transceivertype_bulk_edit'),
    path('transceivertype/<int:pk>/', views.TransceiverTypeView.as_view(), name='transceivertype'),
    path('transceivertype/<int:pk>/edit/', views.TransceiverTypeEditView.as_view(), name='transceivertype_edit'),
    path('transceivertype/<int:pk>/delete/', views.TransceiverTypeDeleteView.as_view(), name='transceivertype_delete'),
    path('transceivertype/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='transceivertype_changelog', kwargs={'model': models.TransceiverType}),

    # Transceiver
    path('transceiver/', views.TransceiverListView.as_view(), name='transceiver_list'),
    path('transceiver/add/', views.TransceiverEditView.as_view(), name='transceiver_add'),
    path('transceiver/delete/', views.TransceiverBulkDeleteView.as_view(), name='transceiver_bulk_delete'),
    path('transceiver/edit/', views.TransceiverBulkEditView.as_view(), name='transceiver_bulk_edit'),
    #path('transceiver/<int:pk>/', include(get_model_urls('netbox_transceiver', 'transceiver'))),

    )