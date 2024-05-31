from django.contrib import admin
from .models import Limpieza_puestos, Puestos, Registro_objetos
# Register your models here.
class PuestosAdmin(admin.ModelAdmin):
    list_display = ("nombre_puesto", "estado", "usuario_servicio")

class LimpiezaAdmin(admin.ModelAdmin):
    list_display = ("nombre_limpieza", "estado", "horario_limpieza", "usuario_servicio")
    
    list_filter = ("horario_limpieza",)

class Registro_objetoAdmin(admin.ModelAdmin):
    list_display = ("nombre_objeto", "estado", "tipo_objeto", "puesto", "usuario_servicio")
    list_filter = ("tipo_objeto","estado",)



admin.site.register(Limpieza_puestos, LimpiezaAdmin)
admin.site.register(Puestos, PuestosAdmin)
admin.site.register(Registro_objetos, Registro_objetoAdmin)
