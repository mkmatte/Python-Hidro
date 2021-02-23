from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from control.models import *

# from control.models import DataSensor
from control.api.serializers import DataSensorSerializer
from control.api.serializers import RegisterControllerSerializer
from rest_framework import mixins
from rest_framework import generics


class SensorViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = DataSensor.objects.all()
    serializer_class = DataSensorSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data_return = self.create(request, *args, **kwargs)
        monitor = VerificationMonitor()
        monitor.verificationMonitor()
        return data_return


class RegisterControllerViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = RegisterController.objects.all()
    serializer_class = RegisterControllerSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
