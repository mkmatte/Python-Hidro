# Generated by Django 3.1.1 on 2021-03-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0003_auto_20210317_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end',
            field=models.CharField(default=None, max_length=30, verbose_name='Agendamento Conforme padrão CronTab'),
        ),
    ]
