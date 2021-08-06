from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Sector)
admin.site.register(MicroController)
admin.site.register(Sensor)
# admin.site.register(SensorConfiguration)
admin.site.register(Actuator)
# admin.site.register(ActuatorConfiguration)
