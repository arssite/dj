from django.urls import path
from . import views

urlpatterns = [path('',views.template_login),
               path('login',views.template_login),
               path('signup',views.template_signup),
]