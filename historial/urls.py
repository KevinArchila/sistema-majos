from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.historial_home, name="home_historial"),
    path('histori_aceite/', views.histori_aceite, name="histori_aceite"),
    path('edit_histori_aceite/<id_registro>', views.edit_histori_aceite, name="edit_histori_aceite"),
    path('delet_aceite/<id_registro>', views.delet_aceite, name="delet_aceite"),
    path('histori_tempe/', views.histori_tempe, name="histori_tempe"),
    path('edit_histori_tempe/<id_registro>', views.edit_histori_tempe, name="edit_histori_tempe"),
    path('delet_tempe/<id_registro>', views.delet_tempe, name="delet_tempe"),
    path('histori_limpie/', views.histori_limpie, name="histori_limpie"),
    path('edit_histori_limpie/<id_registro>', views.edit_histori_limpie, name="edit_histori_limpie"),
    path('delet_limpie/<id_registro>', views.delet_limpie, name="delet_limpie"),
]
