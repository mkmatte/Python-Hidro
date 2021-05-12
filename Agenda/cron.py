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
            arquivo.write(schedule.tag_schedule + " - True - " + str(now) + "\n")
            actionActuators(schedule.actions_start)

        if croniter.match(schedule.end, now):
            arquivo.write(schedule.tag_schedule + " - False - " + str(now) + "\n")
            actionActuators(schedule.actions_end)
    arquivo.close()
