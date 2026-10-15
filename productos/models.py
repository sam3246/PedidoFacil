from django.db import models

class productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField()
    precio = models.FloatField()
    stock = models.IntegerField()
    fecha_registro = models.DateField()