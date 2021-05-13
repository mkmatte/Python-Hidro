from .models import *
from datetime import datetime
from croniter import croniter
from control.monitor import actionActuators


def Execution():
    arquivo = open("/home/saac/Documents/Agenda.log", "a")

    # arquivo.write("Cron - ")
    allSchedule = Schedule.objects.all()
    now = datetime.now()
    for schedule in allSchedule:
        if croniter.match(schedule.start, now):
            print("Agenda 0")
            arquivo.write(schedule.tag_schedule + " 2- True - " + str(now) + "\n")
            print("Agenda 1")
            actionActuators(schedule.actions_start.all())

        if croniter.match(schedule.end, now):
            arquivo.write(schedule.tag_schedule + " - 2 False - " + str(now) + "\n")
            actionActuators(schedule.actions_end.all())
    arquivo.close()
