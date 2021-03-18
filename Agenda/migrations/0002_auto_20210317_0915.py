# Generated by Django 3.1.1 on 2021-03-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='day_end',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='day_start',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='hours_end',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='hours_start',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='min_end',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='min_start',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='month_end',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='month_start',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='week_end',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='week_start',
        ),
        migrations.AddField(
            model_name='schedule',
            name='end',
            field=models.CharField(default=None, max_length=10, null=True, verbose_name='Agendamento Conforme padrão CronTab'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='start',
            field=models.CharField(default='* * * * *', max_length=10, null=True, verbose_name='Agendamento Conforme padrão CronTab'),
        ),
    ]
