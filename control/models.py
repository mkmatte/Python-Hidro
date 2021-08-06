from django.db import models
from monitor.models import *
from data.models import *
from data.models import MicroController
from control.models import *
import requests
import datetime
import json
from django.http import HttpResponse


class DataSensor(models.Model):
    controller = models.ForeignKey(MicroController, null=True, on_delete=models.SET_NULL)
    sensor = models.ForeignKey(Sensor, null=True, on_delete=models.SET_NULL)
    value = models.TextField(max_length=100, null=True)
    verification = False
    data_type = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)

    def update(self, new):
        self.verification = new

    def __str__(self):
        return (
            str(self.controller)
            + " : "
            + str(self.sensor)
            + " : "
            + self.value
            + " "
            + str(self.verification)
            + " "
            + self.data_type
            + " : "
            + self.date_created.__str__()
        )


class DataActuador(models.Model):
    controller = models.ForeignKey(MicroController, null=True, on_delete=models.SET_NULL)
    actuator = models.ForeignKey(Actuator, null=True, on_delete=models.SET_NULL)
    active_status = models.BooleanField(default=False)
    value = models.CharField(max_length=100, null=True)
    data_type = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return (
            str(self.controller)
            + " : "
            + str(self.actuator)
            + " : "
            + str(self.value)
            + " "
            + self.date_created.__str__()
        )


class RegisterController(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    mac_address = models.TextField(max_length=17, null=True)
    controller = models.ForeignKey(MicroController, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (
            str(self.ip_address)
            + " - "
            + str(self.controller.__str__())
            + " : "
            + self.date_created.__str__()
        )


class Log(models.Model):
    controller = models.ForeignKey(MicroController, null=True, on_delete=models.SET_NULL)
    logging = models.TextField(max_length=2000, null=True)
    type_log = models.TextField(max_length=2000, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):

        return self.date_created.__str__() + " : " + str(self.type_log) + " : " + str(self.logging)
