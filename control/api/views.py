from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from control.models import *
from control.monitor import verificationMonitor
from monitor.models import *
from data.models import *
from control.models import *
from rest_framework.decorators import action

# from control.models import DataSensor
from control.api.serializers import DataSensorSerializer
from control.api.serializers import DataActuatorSerializer
from control.api.serializers import RegisterControllerSerializer
from control.api.serializers import LogSerializer
from rest_framework import mixins
from rest_framework import generics
from json import dumps


class SensorViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = DataSensor.objects.all()
    serializer_class = DataSensorSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    # @action(detail=True, methods=['post'])
    # def create(self, request, *args, **kwargs):
    #     sensor_data = request.data
    #
    #     new_data = self.objects.create(
    #         controller=sensor_data["controller"],
    #         sensor=sensor_data["sensor"],
    #         value=sensor_data["value"],
    #         data_type=sensor_data["datatype"],
    #         verification=False,
    #     )
    #     new_data.save()
    #     print(new_data)
    #     serializer = DataSensorSerializer(new_data)
    #     return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        new_data_sensor = self.create(request, *args, **kwargs)
        verificationMonitor(request.data)
        return new_data_sensor


class ActuatorViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = DataActuador.objects.all()
    serializer_class = DataActuatorSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RegisterControllerViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = RegisterController.objects.all()
    serializer_class = RegisterControllerSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LogViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
