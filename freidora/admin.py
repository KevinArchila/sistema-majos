from django.contrib import admin
from .models import Cambio_aceite

# Register your models here.
class Cambio_aceiteAdmin(admin.ModelAdmin):
    list_display = ("registro_objeto", "fecha", "usuario", "horario", "estado", "usuario_servicio")
    list_filter = ("fecha", "usuario_servicio", "estado",)

admin.site.register(Cambio_aceite, Cambio_aceiteAdmin)
