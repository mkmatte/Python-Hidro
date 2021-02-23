# from django.shortcuts import render
#
# from django.http import HttpResponse
# from rest_framework import viewsets
#
# # from data.models import *
# from .serializers import DataSensorSerializer
# from control.models import *
# from rest_framework import generics
# from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


# class DataSensorViewSet(generics.ListCreateAPIView):
#     queryset = DataSensor.objects.all()
#     serializer_class = DataSensorSerializer
#
#     def post(self, request, *args, **kwargs):
#         # added function here
#         # print("Teste Serializer")
#         # monitor = VerificationMonitor()
#         # monitor.verificationMonitor()
#         return self.create(request, *args, **kwargs)
