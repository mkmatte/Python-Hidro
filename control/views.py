from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from data.models import Sensor
from .utils import get_plot
import matplotlib
import pandas as pd

# Create your views here.
class form_Project(forms.Form):
    class Meta:
        model= Project
        

def data_sensor(request):
    graphs = []
    sensor = Sensor.objects.all()
    for s in sensor:
        try:
            qs = DataSensor.objects.filter(sensor=s.id).order_by('-id')[:30]
        except:
            qs = DataSensor.objects.filter(sensor=s.id)
        list_of_datetimes = [x.date_created for x in qs]
        x = pd.to_datetime(list_of_datetimes, format="%d-%m %H:%M")
        y = [float(y.value) for y in qs]
        tag_plot = s.tag_sensor +' : '+s.controller.label_controller +' ('+ s.controller.sector.project.name_project +')'
        chart = get_plot(x,y,tag_plot,qs[0].data_type)
        graphs.append(chart)
    return render(request,"main/data_sensor.html",{'graphs':graphs})


def data_actuator(request):
    graphs = []
    actuator = Actuator.objects.all()
    for s in actuator:
        try:
            qs = DataActuador.objects.filter(actuator=s.id).order_by('-id')[:20]
        except:
            qs = DataActuador.objects.filter(actuator=s.id)
        list_of_datetimes = [x.date_created for x in qs]
        x = pd.to_datetime(list_of_datetimes, format="%d-%m %H:%M")
        y = [float(y.value) for y in qs]
        tag_plot = s.tag_actuator +' : '+s.controller.label_controller +' ('+ s.controller.sector.project.name_project +')'
        chart = get_plot(x,y,tag_plot,qs[0].data_type)
        graphs.append(chart)
    return render(request,"main/data_actuator.html",{'graphs':graphs})    
    
    
    
    # if request.method == 'GET':
    #     projects = Project.objects.all()
    #     return render(
    #         request,
    #         "main/data.html",
    #         {"projects": projects},
    #     )
    # if request.method == 'POST':
    #     form = form_Project()