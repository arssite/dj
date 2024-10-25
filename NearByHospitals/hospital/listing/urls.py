from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital_list, name='hospital_list'),
]
