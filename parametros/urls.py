from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.parametros_home, name="home_parametros"), 
    path('salir_parametros/', views.salir_parametros, name="salir_parametros"),
    path('login_paramet/', views.login_paramet, name="login_paramet"),
    path('tempe_neveras/', views.tempe_neveras, name="tempe_neveras"),
    path('segui_aceite/', views.segui_aceite, name="segui_aceite"),
    path('puestos/', views.puestos, name="puestos"),
    path('cargos/', views.cargos, name="cargos"),
    path('limpie_puesto/', views.limpie_puesto, name="limpie_puesto"),
    path('perfil/', views.perfil, name="perfil"),
    path('registro_nevera/', views.registro_nevera, name="registro_nevera"),
    path('registro_freidora/', views.registro_freidora, name="registro_freidora"),
    path('registro_puesto/', views.registro_puesto, name="registro_puesto"),
    path('registro_cargo/', views.registro_cargo, name="registro_cargo"),
    path('registro_limpieza/', views.registro_limpieza, name="registro_limpieza"),
    path('registro_perfil/', views.registro_perfil, name="registro_perfil"),
    path('prueba/', views.prueba),
]
