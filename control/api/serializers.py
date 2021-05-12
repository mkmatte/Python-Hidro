from rest_framework import serializers
from control.models import *


class DataSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSensor
        fields = '__all__'


class DataActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataActuador
        fields = '__all__'


class RegisterControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterController
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
