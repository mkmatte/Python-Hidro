from django.db import models
from monitor.models import Action
from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django import forms

# Create your models here.


class Schedule(models.Model):

    tag_schedule = models.CharField(max_length=100, null=True)

    # Agenda Padrão Crontab Linux
    start = models.CharField(
        max_length=30,
        null=True,
        default="* * * * *",
        verbose_name="Agendamento Conforme padrão CronTab",
    )

    # tempo em minutos para reverter a tarefa
    # Agenda Padrão Crontab Linux
    end = models.CharField(
        max_length=30,
        null=False,
        blank=True,
        default=None,
        verbose_name="Agendamento Conforme padrão CronTab",
    )

    actions_start = models.ManyToManyField(Action, related_name='tag_schedule')
    actions_end = models.ManyToManyField(
        Action, related_name='tag_schedule2', null=False, blank=True
    )

    def __str__(self):
        return self.tag_schedule


class ScheduleAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'actions_start',
        'actions_end',
    )
