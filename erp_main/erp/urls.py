
from django.urls import path
from . import views
from .views import CreateJobFileView


urlpatterns = [
    path('', views.home, name=''),
    path('file_ref_no/', views.file_ref_no, name='file_ref_no'),
    path('client/', views.client, name='client'),
    path('cargo_type/', views.cargo_type, name='cargo_type'),
    path('cargo_classification/', views.cargo_classification, name='cargo_classification'),
    path('from_location/', views.from_location, name='from_location'),
    path('to_location/', views.to_location, name='to_location'),
    path('route/', views.route, name='route'),
    path('operations_dashboard/', views.operations_dashboard, name='operations_dashboard'),
    path('create-job-file/', CreateJobFileView.as_view(), name='create-job-file'),
    path('edit-job-file/<uuid:file_id>/', CreateJobFileView.as_view(), name='edit-job-file'),
]