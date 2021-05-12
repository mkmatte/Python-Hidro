from django.db import models

# Create your models here.


class Project(models.Model):
    name_project = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=2000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name_project + " : " + self.description


class Sector(models.Model):
    name_sector = models.CharField(max_length=200, null=True)
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=2000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name_sector + " : " + self.description


class MicroController(models.Model):
    sector = models.ForeignKey(Sector, null=True, on_delete=models.SET_NULL)
    label_controller = models.CharField(max_length=200, null=True)
    model_controller = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=2000, null=True)
    mac = models.CharField(max_length=20, null=True)
    chip_id = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(verbose_name='Controlador Ativo?', default=False)

    def __str__(self):
        return (
            str(self.id)
            + " : "
            + self.model_controller
            + " : "
            + self.label_controller
            + " : "
            + self.description
        )


class Sensor(models.Model):
    controller = models.ForeignKey(MicroController, null=True, on_delete=models.SET_NULL)
    tag_sensor = models.CharField(max_length=100, null=True)
    type_sensor = models.CharField(max_length=100, null=True)
    model_sensor = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=2000, null=True)
    port_sensor = models.CharField(max_length=100, null=True)
    description_port = models.TextField(max_length=2000, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return (
            str(self.id)
            + '-'
            + self.type_sensor
            + " : "
            + self.description
            + " : "
            + self.model_sensor
        )


class SensorConfiguration(models.Model):
    tag_config_sensor = models.CharField(max_length=100, null=True)
    sensor = models.ForeignKey(Sensor, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, null=True)
    time_read_sensor = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.tag_config_sensor


class Actuator(models.Model):
    controller = models.ForeignKey(MicroController, null=True, on_delete=models.SET_NULL)
    tag_actuator = models.CharField(max_length=100, null=True)
    type_actuator = models.CharField(max_length=100, null=True)
    model_actuator = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=2000, null=True)
    port_actuator = models.CharField(max_length=100, null=True)
    description_port = models.TextField(max_length=2000, null=True)
    active_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return (
            str(self.id)
            + ' - '
            + self.type_actuator
            + " : "
            + self.description
            + " : "
            + self.model_actuator
        )


class ActuatorConfiguration(models.Model):
    tag_config_actuator = models.CharField(max_length=100, null=True)
    actuator = models.ForeignKey(Actuator, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, null=True)
    # time_read_sensor = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.tag_config_actuator
