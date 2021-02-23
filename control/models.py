from django.db import models
from monitor.models import *
from data.models import *
from control.models import *
import requests
import datetime
import json
from django.http import HttpResponse


class DataSensor(models.Model):
    controller = models.ForeignKey(MicroController, null=True, on_delete=models.SET_NULL)
    sensor = models.ForeignKey(Sensor, null=True, on_delete=models.SET_NULL)
    data = models.TextField(max_length=100, null=True)
    data_type = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return (
            str(self.controller.label_controller)
            + " : "
            + str(self.sensor.type_sensor)
            + " : "
            + self.data
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
    date_created = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)


class RegisterController(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    mac_address = models.TextField(max_length=17, null=True)
    controller = models.ForeignKey(MicroController, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (
            self.ip_address
            + " - "
            + self.controller.label_controller
            + " : "
            + self.date_created.__str__()
        )


class VerificationMonitor(models.Model):
    from paho.mqtt import client as mqtt_client

    def verificationMonitor(self):
        allMonitor = RulesMonitor.objects.all()
        print(allMonitor)
        for monitor in allMonitor:
            rules = monitor.rules.all()
            action = self.verificationRules(rules)
            print(str(action))
            if action == True:
                self.actionActuators(monitor.actionsTrue.all())
            else:
                self.actionActuators(monitor.actionsFalse.all())

    def verificationRules(self, rules):
        action = True
        for rule in rules:
            print("--------" + str(rule))
            datasensor = DataSensor.objects.filter(sensor=rule.sensor.id).last()

            if rule.condition == str(1):
                if float(datasensor.data) > float(rule.value):
                    action = action and True
                else:
                    action = action and False
            elif rule.condition == str(2):
                if float(datasensor.data) >= float(rule.value):
                    action = action and True
                else:
                    action = action and False
            elif rule.condition == str(3):
                if float(datasensor.data) < float(rule.value):
                    action = action and True
                else:
                    action = action and False
            elif rule.condition == str(4):
                if float(datasensor.data) <= float(rule.value):
                    action = action and True
                else:
                    action = action and False
            elif rule.condition == str(5):  # =
                if datasensor.data == "True" or datasensor.data == "False":
                    if datasensor.data == rule.value:
                        action = action and True
                    else:
                        action = action and False
                else:
                    if float(datasensor.data) == float(rule.value):
                        action = action and True
                    else:
                        action = action and False
            elif rule.condition == str(6):
                if datasensor.data == "True" or datasensor.data == "False":
                    if datasensor.data != rule.value:
                        action = action and True
                    else:
                        action = action and False
                else:
                    if float(datasensor.data) != float(rule.value):
                        action = action and True
                    else:
                        action = action and False
        return action

    def actionActuators(self, actions):
        import json

        print(self)
        for action in actions:
            print(action.actuator.controller.mac)
            ip_address = RegisterController.objects.filter(
                mac_address=action.actuator.controller.mac
            ).last()
            print(action)
            print("Controller:" + str(action.actuator.controller.id))
            print("ID Actuator: " + str(action.actuator.id))
            data = {}
            data['controller'] = action.actuator.controller.id
            data['actuator'] = action.actuator.id
            data['status'] = action.new_status
            data['value'] = action.value
            # data["date_created"] = datetime.datetime.now()
            json = json.dumps(data, indent=4)
            broker = '192.168.1.107'
            port = 1883
            topic = str(action.actuator.controller.id)
            client_id = f'server'

            import paho.mqtt.client as paho

            def on_publish(client, userdata, result):  # create function for callback
                print("data published \n")
                pass

            client1 = paho.Client("control1")  # create client object
            client1.on_publish = on_publish  # assign function to callback
            client1.connect(broker, port)  # establish connection
            if action.new_status == "1":
                ret = client1.publish(topic, b'1')  # publish
            else:
                ret = client1.publish(topic, b'0')  # publish
