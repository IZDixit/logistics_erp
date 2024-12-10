
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=''),
    path('job_information/', views.job_information, name='job_information'),
<<<<<<< HEAD
    path('supplier_information/', views.supplier_information, name='supplier_information'),
    path('loose_cargo_information/', views.loose_cargo_information, name='loose_cargo_information'),
    path('container_details/', views.container_details, name='container_details'),
=======
>>>>>>> ac324d95e26da2378cb43c0ac40f0506e4bd67c4
    path('file_ref_no/', views.file_ref_no, name='file_ref_no'),
    path('client/', views.client, name='client'),
    path('cargo_type/', views.cargo_type, name='cargo_type'),
    path('cargo_classification/', views.cargo_classification, name='cargo_classification'),
    path('from_location/', views.from_location, name='from_location'),
    path('to_location/', views.to_location, name='to_location'),
    path('route/', views.route, name='route'),
]