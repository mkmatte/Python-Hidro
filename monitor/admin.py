from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from django.utils.translation import ugettext_lazy as _

# Register your models here.

from .models import *


admin.site.register(Rule)
admin.site.register(Action)
# admin.site.register(ScheduleAction)
admin.site.register(RulesMonitor, RulesMonitorAdmin)
