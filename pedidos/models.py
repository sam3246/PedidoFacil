from django.db import models

class pedidos(models.Model):
    num_pedido = models.IntegerField()
    cliente = models.CharField()
    fecha_pedido = models.DateField()
    descripcion_pedido = models.CharField()
    valor = models.FloatField()
    estado = models.CharField()
    registrador = models.CharField