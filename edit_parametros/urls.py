from django.urls import path
from . import views

urlpatterns = [
    path('edit_limpieza/<id_limpieza>', views.edit_limpieza, name="edit_limpieza"),
    path('delet_limpieza/<id_limpieza>', views.delet_limpieza, name="delet_limpieza"),
    path('edit_freidora/<id_freidora>', views.edit_freidora, name="edit_freidora"),
    path('reparar_freidora/<id_freidora>', views.reparar_freidora, name="reparar_freidora"),
    path('operativo_freidora/<id_freidora>', views.operativo_freidora, name="operativo_freidora"), 
    path('delet_freidora/<id_freidora>', views.delet_freidora, name="delet_freidora"),
    path('edit_nevera/<id_nevera>', views.edit_nevera, name="edit_nevera"),
    path('reparar_nevera/<id_nevera>', views.reparar_nevera, name="reparar_nevera"),
    path('operativo_nevera/<id_nevera>', views.operativo_nevera, name="operativo_nevera"), 
    path('delet_nevera/<id_nevera>', views.delet_nevera, name="delet_nevera"),
    path('edit_puesto/<id_puesto>', views.edit_puesto, name="edit_puesto"),
    path('delet_puesto/<id_puesto>', views.delet_puesto, name="delet_puesto"),
    path('edit_cargo/<id_cargo>', views.edit_cargo, name="edit_cargo"),
    path('delet_cargo/<id_cargo>', views.delet_cargo, name="delet_cargo"),
    path('edit_perfil/<id_perfil>', views.edit_perfil, name="edit_perfil"),
    path('delet_perfil/<id_perfil>', views.delet_perfil, name="delet_perfil"),
]
