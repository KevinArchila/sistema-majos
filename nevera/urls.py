from django.urls import path
from . import views

urlpatterns = [
    path('cambio_tempe/<id_puesto>', views.nevera_tempe, name="cambio_tempe"),  
]
