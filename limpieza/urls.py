from django.urls import path
from . import views

urlpatterns = [
    path('limpieza_puestos/<id_puesto>', views.registro_limpiezas, name="limpieza_puestos"),  
]
