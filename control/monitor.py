from monitor.models import *
from data.models import *
from control.models import *
import subprocess
import platform    # For getting the operating system name


def verificationMonitor(data_sensor):

    allMonitor = RulesMonitor.objects.all()
    for monitor in allMonitor:
        rules = monitor.rules.all()
        for rule in rules:
            if rule.sensor.id == int(data_sensor['sensor']):
                action = verificationRules(rules)
                if action == True:
                    actionActuators(monitor.actionsTrue.all())
                else:
                    actionActuators(monitor.actionsFalse.all())


def verificationRules(rules):
    action = True
    for rule in rules:
        datasensor = DataSensor.objects.filter(sensor=rule.sensor.id).last()
        if rule.condition == str(1):
            if float(datasensor.value) > float(rule.value):
                action = action and True
            else:
                action = action and False
        elif rule.condition == str(2):
            if float(datasensor.value) >= float(rule.value):
                action = action and True
            else:
                action = action and False
        elif rule.condition == str(3):
            if float(datasensor.value) < float(rule.value):
                action = action and True
            else:
                action = action and False
        elif rule.condition == str(4):
            if float(datasensor.value) <= float(rule.value):
                action = action and True
            else:
                action = action and False
        elif rule.condition == str(5):  # =
            if datasensor.value == "True" or datasensor.value == "False":
                if datasensor.value == rule.value:
                    action = action and True
                else:
                    action = action and False
            else:
                if float(datasensor.value) == float(rule.value):
                    action = action and True
                else:
                    action = action and False
        elif rule.condition == str(6):
            if datasensor.value == "True" or datasensor.value == "False":
                if datasensor.value != rule.value:
                    action = action and True
                else:
                    action = action and False
            else:
                if float(datasensor.value) != float(rule.value):
                    action = action and True
                else:
                    action = action and False
    return action


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
        if not action.value is None: data['value'] = action.value
        #data_test = "{\"control_on\":\"True\", \"control_off\":\"True\"}"
        if not action.data is None: data.update(json.loads(action.data))

        # data["date_created"] = datetime.datetime.now()
        json = json.dumps(data, indent=4)
        broker = '192.168.100.100'
        port = 1883
        topic = str(data['controller'])
        client_id = f'server'

        import paho.mqtt.client as paho

        def on_publish(client, userdata, result):  # create function for callback
            print("data published \n")
            # print(userdata)
            pass

        client1 = paho.Client("control1")  # create client object
        client1.on_publish = on_publish  # assign function to callback
        client1.connect(broker, port)  # establish connection
        client1.publish(topic, json)
        print(json)


def telegram_message(msg):
    import requests

    token = "1847502844:AAFX6i9t5g0Gdv3NQfeqyFR6xf1YKruHic0"
    group_id = "-552068730"
    url = (
        "https://api.telegram.org/bot"
        + str(token)
        + "/sendMessage?chat_id="
        + str(group_id)
        + "&text="
        + str(msg)
    )
    requests.post(url)


def notification_sensor_telegram(data):
    datasensor = Sensor.objects.filter(id=data['sensor']).last()
    print(datasensor)
    if datasensor.send_message == True:
        telegram_message(data)


def notification_actuator_telegram(data):
    dataactuator = Actuator.objects.filter(id=data['actuator']).last()
    print(dataactuator)
    if dataactuator.send_message == True:
        telegram_message(data)


def verification_controller():
    controllers = MicroController.objects.all()
    for c in controllers:
        try:
            rc = RegisterController.objects.filter(controller=c).last()
            if rc == None: continue
            if rc.controller.status == True:    
                situation = ping(rc.ip_address)
                if situation == False:
                    msg = rc.controller.label_controller +" : "+ rc.ip_address + ": Não está respondo, acorda aquele priguiçoso..."
                    telegram_message(msg)
        except:
            pass



def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '4', host]

    return subprocess.call(command) == 0    