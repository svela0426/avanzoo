from unittest.util import _MAX_LENGTH
from django.db import models
from cliente.models import Cliente

# Create your models here.

class Solicitud(models.Model):
    cliente=models.ForeignKey( Cliente, on_delete=models.CASCADE, default=None)
    monto= models.FloatField(null=True, blank=True , default=None)
    fecha=models.DateTimeField(auto_now_add=True)
    cuotas=models.FloatField(null=True, blank=True , default=None)
    estado=models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.monto, self.estado)
