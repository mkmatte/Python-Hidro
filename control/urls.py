from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("sensor", views.data_sensor, name="home"),
    path("actuator", views.data_actuator, name="atuador")
]