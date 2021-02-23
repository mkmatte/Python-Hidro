from rest_framework import serializers
from control.models import *


class DataSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSensor
        fields = '__all__'


class RegisterControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterController
        fields = '__all__'
