from monitor.forms import ActionForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from control.monitor import actionActuators

# Create your views here


def monitor(response):
    monitors = RulesMonitor.objects.all()
    rules = Rule.objects.all()
    actions = Action.objects.all()


    return render(
        response,
        "main/monitor_index.html",
        {"monitors": monitors, "rules": rules, "actions": actions},
    )

def actions(request):
    if request.user.is_authenticated == False:
        return redirect('/admin/')


    form = ActionForm() 

    exec = False  
    if request.method == 'POST':
        print('POST: ',request.POST)
        ac = Action.objects.filter(id = request.POST['id'])      
        actionActuators(ac)
        exec = True
        

    
    actions = Action.objects.all()
    return render(
        request,
        "main/action.html",
        {'exec':exec, "actions": actions},
    )
