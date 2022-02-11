from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from data.models import Sensor
from data.models import Project
from .utils import get_plot
import matplotlib
import pandas as pd

# Create your views here.
class form_Project(forms.Form):
    class Meta:
        model= Project
        

def data_sensor(request):
    print('POST: ',request.POST)
    all_dados = []
    
    if request.method == 'POST':
        sensor = Sensor.objects.filter(controller__sector__project__id = request.POST['projeto'])      
    else:
        sensor = Sensor.objects.all()
    projetos = Project.objects.all()
    for s in sensor:
        graphs = []
        dados=[]
        tag_sensor = []
        try:
            qs = DataSensor.objects.filter(sensor=s.id).order_by('-id')[:20]
        except:
            qs = DataSensor.objects.filter(sensor=s.id)
        dados.append(qs)
        list_of_datetimes = [x.date_created for x in qs]
        x = pd.to_datetime(list_of_datetimes, format="%d-%m %H:%M")
        y = [float(y.value) for y in qs]
        tag_plot = s.tag_sensor +' : '+s.controller.label_controller +' ('+ s.controller.sector.project.name_project +')'
        chart = get_plot(x,y,tag_plot,qs[0].data_type)
        graphs.append(chart)        
        q = qs[0]
        tag_sensor.append(q.sensor.tag_sensor)
        all_dados.append(zip(graphs,dados,tag_sensor))
    print(len(all_dados))
    return render(request,"main/data_sensor.html",{'all_dados':all_dados, "projetos": projetos})


def data_actuator(request):

    all_dados = []

    if request.method == 'POST':
        actuator = Actuator.objects.filter(controller__sector__project__id = request.POST['projeto'])      
    else:
        actuator = Actuator.objects.all()
    projetos = Project.objects.all()
    for s in actuator:
        graphs = []
        dados=[]
        tag_actuator = []
        try:
            qs = DataActuador.objects.filter(actuator=s.id).order_by('-id')[:20]
        except:
            qs = DataActuador.objects.filter(actuator=s.id)
        dados.append(qs)
        list_of_datetimes = [x.date_created for x in qs]
        x = pd.to_datetime(list_of_datetimes, format="%d-%m %H:%M")
        y = [float(y.value) for y in qs]
        tag_plot = s.tag_actuator +' : '+s.controller.label_controller +' ('+ s.controller.sector.project.name_project +')'
        chart = get_plot(x,y,tag_plot,qs[0].data_type)
        graphs.append(chart)
        q = qs[0]
        tag_actuator.append(q.actuator.tag_actuator)
        all_dados.append(zip(graphs,dados,tag_actuator))
        
    return render(request,"main/data_actuator.html",{'all_dados':all_dados, "projetos": projetos})    
    
    
    
    # if request.method == 'GET':
    #     projects = Project.objects.all()
    #     return render(
    #         request,
    #         "main/data.html",
    #         {"projects": projects},
    #     )
    # if request.method == 'POST':
    #     form = form_Project()