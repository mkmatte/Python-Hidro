# Generated by Django 3.1.1 on 2020-10-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_registercontroller_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registercontroller',
            name='mac_address',
            field=models.TextField(max_length=17, null=True),
        ),
    ]
