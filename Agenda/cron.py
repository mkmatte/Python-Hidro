from .models import *
from datetime import datetime
from croniter import croniter


def Execution():
    arquivo = open("/home/saac/Documents/Agenda.log", "a")

    # arquivo.write("Cron - ")
    allSchedule = Schedule.objects.all()
    now = datetime.now()
    for schedule in allSchedule:
        if croniter.match(schedule.start, now):
            arquivo.write(schedule.tag_schedule + " - True - " + str(now) + "\n")
        if croniter.match(schedule.end, now):
            arquivo.write(schedule.tag_schedule + " - False - " + str(now) + "\n")
    arquivo.close()


def teste():
    arquivo = open("Agenda.log", "a")
    arquivo.write("Cron Funcionou \n")
    arquivo.close()


def actionActuators(actions):
    import json

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
