from django.db import models
from parametros.models import Registro_objetos
from login.models import Usuario_servicio, Usuarios

# Create your models here.
class Cambio_aceite(models.Model):
    registro_objeto = models.ForeignKey(Registro_objetos, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    fecha = models.DateField()
    puesto = models.CharField(max_length=20)
    horario = models.CharField(max_length=15)
    estado = models.CharField(max_length=6)
    usuario_servicio = models.ForeignKey(Usuario_servicio, on_delete=models.DO_NOTHING)