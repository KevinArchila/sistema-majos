from django.shortcuts import render, redirect
from parametros.models import Puestos, Registro_objetos
from .models import Cambio_aceite
import datetime

# Create your views here.

def cambi_aceite(request, id_puesto):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(estado = "True", usuario_servicio = usuario_servicio_id)
    if id_puesto == "inicio":
        return render(request, "segui_aceite.html", {"puestos": puestos, "inicio": "Selecciona un puesto"})
    else:
        select_puesto = Puestos.objects.filter(id=id_puesto, usuario_servicio = usuario_servicio_id).first()
        freidoras = Registro_objetos.objects.filter(puesto = id_puesto, estado = "True", servicio = "Operativo", tipo_objeto = "Freidora", usuario_servicio = usuario_servicio_id)
        if request.method == "POST":
            freidora_select = request.POST.get("opcion")
            fecha_actual = datetime.date.today()
            horario = request.POST.get("horario")
            perfil = request.session.get("id_perfil")
            if freidora_select is not None:
                puesto = Registro_objetos.objects.filter(id = freidora_select).first() 
                cambi_aceite = Cambio_aceite(registro_objeto_id = freidora_select, usuario_id = perfil, fecha = fecha_actual, horario = horario, estado = "True", puesto = puesto.puesto.nombre_puesto, usuario_servicio_id = usuario_servicio_id)
                cambi_aceite.save()
                return render(request, "segui_aceite.html", {"freidoras": freidoras, "puestos": puestos, "select_puesto": select_puesto, "mensaje_exito": "Cambio de Aceite Registrado"})   
            else:
                return render(request, "segui_aceite.html", {"freidoras": freidoras, "puestos": puestos, "select_puesto": select_puesto, "mensaje": "No seleccionaste ninguna freidora"})
        return render(request, "segui_aceite.html", {"freidoras": freidoras, "puestos": puestos, "select_puesto": select_puesto})