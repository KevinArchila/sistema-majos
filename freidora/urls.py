from django.urls import path
from . import views

urlpatterns = [
    path('cambi_aceite/<id_puesto>', views.cambi_aceite, name="cambi_aceite"),  
]
