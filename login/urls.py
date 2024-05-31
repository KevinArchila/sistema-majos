from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_servicio, name="Servicio"),
    path('login_usuario/', views.inicio_servicio, name="login_usuario"),
    path('cerrar/', views.cerrar, name="cerrar"),
    path('perfiles/', views.perfiles_usuarios, name="perfiles"),
    path('agregar_perfil/', views.agregar_perfil, name="agregar_perfil"),
    path('login_perfil/<perfil_id>', views.login_perfil, name="login_perfil"),
    path('log_out_servicio/', views.log_out_servicio, name="log_out_servicio"),
]
