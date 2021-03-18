from django.db import models
from django.contrib import admin

from django import forms

from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from data.models import *


# Create your models here.


class Rule(models.Model):

    CONDITIONS = (
        ("1", ">"),
        ("2", "≥"),
        ("3", "<"),
        ("4", "≤"),
        ("5", "="),
        ("6", "!="),
    )
    tag_rule = models.CharField(max_length=100, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=True)
    # data = models.ForeignKey(Sensor.id_sensor, ull=True, on_delete=models.SET_NULL)
    condition = models.CharField(max_length=1, choices=CONDITIONS, blank=False, null=False)
    value = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.tag_rule


class Action(models.Model):
    tag_action = models.CharField(max_length=100, null=True)
    actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE, null=True)
    new_status = models.CharField(
        max_length=100, null=True, verbose_name="Status (1-True; 0-False)"
    )
    value = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.tag_action


class RulesMonitor(models.Model):
    tag_monitor = models.CharField(max_length=100, null=True)
    rules = models.ManyToManyField(Rule, related_name='tag_monitor')
    actionsTrue = models.ManyToManyField(Action, related_name='tag_monitor')
    actionsFalse = models.ManyToManyField(Action, related_name='tag_monitor2')

    # def ValidationRule(self):
    #     allRules = {}

    def __str__(self):
        return self.tag_monitor


class RulesMonitorAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'rules',
        'actionsTrue',
        'actionsFalse',
    )
    # filter_horizontal = ('actions',)


# class ScheduleAction(models.Model):
#     tag_schedule = models.CharField(max_length=100, null=True)
#     actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE, null=True)
#     time_action = forms.DateTimeField(widget=AdminTimeWidget())
#     new_status = models.CharField(max_length=100, null=True)
#     time_value = models.CharField(max_length=100, null=True)
#     after_status = models.CharField(max_length=100, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     date_updated = models.DateTimeField(auto_now=True, null=True)
