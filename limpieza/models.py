from django.db import models
from parametros.models import Limpieza_puestos
from login.models import Usuarios, Usuario_servicio
# Create your models here.

class Registro_limpieza(models.Model):
    limpieza_puestos = models.ForeignKey(Limpieza_puestos, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    fecha = models.DateField()
    puesto = models.CharField(max_length=20)
    horario = models.CharField(max_length=15)
    estado = models.CharField(max_length=6)
    usuario_servicio = models.ForeignKey(Usuario_servicio, on_delete=models.DO_NOTHING)