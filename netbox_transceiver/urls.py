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

    # TransceiverTypesProfile
    path('transceivertypeprofile/', views.TransceiverTypeProfileListView.as_view(), name='transceivertypeprofile_list'),
    path('transceivertypeprofile/add/', views.TransceiverTypeProfileEditView.as_view(), name='transceivertypeprofile_add'),
    path('transceivertypeprofile/delete/', views.TransceiverTypeProfileBulkDeleteView.as_view(), name='transceivertypeprofile_bulk_delete'),
    path('transceivertypeprofile/edit/', views.TransceiverTypeProfileBulkEditView.as_view(), name='transceivertypeprofile_bulk_edit'),
    path('transceivertypeprofile/<int:pk>/', views.TransceiverTypeProfileView.as_view(), name='transceivertypeprofile'),
    path('transceivertypeprofile/<int:pk>/edit/', views.TransceiverTypeProfileEditView.as_view(), name='transceivertypeprofile_edit'),
    path('transceivertypeprofile/<int:pk>/delete/', views.TransceiverTypeProfileDeleteView.as_view(), name='transceivertypeprofile_delete'),
    path('transceivertypeprofile/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='transceivertypeprofile_changelog', kwargs={'model': models.TransceiverTypeProfile}),

    # Transceiver
    path('transceiver/', views.TransceiverListView.as_view(), name='transceiver_list'),
    path('transceiver/add/', views.TransceiverEditView.as_view(), name='transceiver_add'),
    path('transceiver/delete/', views.TransceiverBulkDeleteView.as_view(), name='transceiver_bulk_delete'),
    path('transceiver/edit/', views.TransceiverBulkEditView.as_view(), name='transceiver_bulk_edit'),
    path('transceiver/<int:pk>/', views.TransceiverView.as_view(), name='transceiver'),
    path('transceiver/<int:pk>/edit/', views.TransceiverEditView.as_view(), name='transceiver_edit'),
    path('transceiver/<int:pk>/delete/', views.TransceiverDeleteView.as_view(), name='transceiver_delete'),
    path('transceiver/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='transceiver_changelog', kwargs={'model': models.Transceiver}),

    )