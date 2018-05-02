from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('pi-tool', views.pi_tool, name='pi_tool'),
        ]
