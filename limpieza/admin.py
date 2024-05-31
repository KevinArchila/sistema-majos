from django.contrib import admin
from .models import Registro_limpieza
# Register your models here.

class Registro_limpiezaAdmin(admin.ModelAdmin):
    list_display = ("limpieza_puestos", "fecha", "usuario", "horario", "estado", "usuario_servicio")
    list_filter = ("fecha", "estado", "usuario_servicio")

admin.site.register(Registro_limpieza, Registro_limpiezaAdmin)