from django.urls import path, include
from .views import *

urlpatterns = [
    path('sensor', SensorViewSet.as_view()),
    path('register', RegisterControllerViewSet.as_view()),
]
