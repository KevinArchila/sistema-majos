from django.contrib import admin
from .models import Cambio_tempe
# Register your models here.

class Cambio_tempeAdmin(admin.ModelAdmin):
    list_display = ("registro_objeto", "temperatura", "puesto", "fecha", "usuario", "horario", "estado", "usuario_servicio")
    list_filter = ("fecha", "usuario", "estado", "usuario_servicio", "puesto")

admin.site.register(Cambio_tempe, Cambio_tempeAdmin)