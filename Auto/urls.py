"""Auto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

# from api.views import DataSensorViewSet


# router = routers.DefaultRouter()
# router.register('DataSensor', DataSensorViewSet)

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('data/', include('control.urls'), name="data"),
    path('admin/', admin.site.urls),
    path('monitor/', include('monitor.urls'), name="monitor"),
    # path('', include('core.urls')),
    # path('data', include('data.urls')),
    # path('monitor', include('monitor.urls')),
    # path('control', include('control.urls')),
    path('sensor', include('control.api.urls')),
    path('api_', include('control.api.urls')),
    # path('datasensor', include(router.urls)),
]
