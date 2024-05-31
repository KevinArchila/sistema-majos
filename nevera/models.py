from django.db import models
from parametros.models import Registro_objetos
from login.models import Usuarios, Usuario_servicio
# Create your models here.

class Cambio_tempe(models.Model):
    registro_objeto = models.ForeignKey(Registro_objetos, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    temperatura = models.CharField(max_length=10)
    fecha = models.DateField()
    horario = models.CharField(max_length=15)
    puesto = models.CharField(max_length=20)
    estado = models.CharField(max_length=6)
    usuario_servicio = models.ForeignKey(Usuario_servicio, on_delete=models.DO_NOTHING)

    
