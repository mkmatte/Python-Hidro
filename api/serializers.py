from rest_framework import serializers
from data.models import *
from monitor.models import *


# class DataSensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DataSensor
#         fields = ['id', 'id_controller', 'id_sensor', 'data', 'data_type', 'date_created']
