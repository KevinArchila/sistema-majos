from django.db import models
from login.models import Usuario_servicio
from django.utils import timezone
# Create your models here.

class Puestos(models.Model):
    nombre_puesto = models.CharField(max_length=20)
    estado = models.CharField(max_length=6)
    usuario_servicio = models.ForeignKey(Usuario_servicio, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre_puesto


class Registro_objetos(models.Model):
    puesto = models.ForeignKey(Puestos, on_delete=models.DO_NOTHING)
    nombre_objeto = models.CharField(max_length=20)
    tipo_objeto = models.CharField(max_length=20)
    servicio = models.CharField(max_length=20)
    estado = models.CharField(max_length=6)
    usuario_servicio = models.ForeignKey(Usuario_servicio, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre_objeto

class Limpieza_puestos(models.Model):
    puesto = models.ForeignKey(Puestos, on_delete=models.DO_NOTHING)
    nombre_limpieza = models.CharField(max_length=30)
    estado = models.CharField(max_length=6)
    horario_limpieza = models.TimeField()
    usuario_servicio = models.ForeignKey(Usuario_servicio, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre_limpieza
    


