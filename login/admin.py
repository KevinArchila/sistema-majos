from django.contrib import admin
from .models import Usuarios, Usuario_servicio, Cargo_usuarios
# Register your models here.
class Usuario_servicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nombre_empresa", "correo", "contraseña", "estado")

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cargo", "contraseña", "estado", "usuario_servicio")

class CargoAdmin(admin.ModelAdmin):
    list_display = ("nombre_cargo", "estado", "usuario_servicio")


admin.site.register(Usuario_servicio, Usuario_servicioAdmin)
admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Cargo_usuarios, CargoAdmin)
