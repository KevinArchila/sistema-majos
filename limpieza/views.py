from django.shortcuts import render, redirect
from parametros.models import Puestos, Limpieza_puestos
from django.utils import timezone
from .models import Registro_limpieza
import datetime

# Create your views here.
def registro_limpiezas(request, id_puesto):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(estado = "True", usuario_servicio = usuario_servicio_id)
    
    hora_actual = datetime.datetime.now().time()
    hora_zona = timezone.now().time()
    fecha = datetime.date.today()
    print(hora_actual)
    print(hora_zona)
    if id_puesto == "inicio":
        return render(request, "registro_limpiezas.html", {"puestos": puestos, "inicio": "Selecciona un puesto"})
    else:
        limpieza_fecha = Registro_limpieza.objects.filter(estado = "True", usuario_servicio = usuario_servicio_id, fecha = fecha)
        lista_fechas = []
        for limpieza_fechas in limpieza_fecha:
            lista_fechas.append(limpieza_fechas.limpieza_puestos.id)
        print(lista_fechas)
        select_puesto = Puestos.objects.filter(id=id_puesto, usuario_servicio = usuario_servicio_id).first()
        limpieza = Limpieza_puestos.objects.filter(puesto = id_puesto, estado = "True", usuario_servicio = usuario_servicio_id)
        if request.method == "POST":
            limpieza_select = request.POST.get("opcion")
            horario = request.POST.get("horario")
            fecha_actual = datetime.date.today()
            perfil = request.session.get("id_perfil")
            if limpieza_select is not None: 
                puesto = Limpieza_puestos.objects.filter(id = limpieza_select).first()
                registrar_limpieza = Registro_limpieza(fecha = fecha_actual, horario = horario, estado = "True", limpieza_puestos_id = limpieza_select, usuario_id = perfil, puesto = puesto.puesto.nombre_puesto, usuario_servicio_id = usuario_servicio_id)
                registrar_limpieza.save()
                limpieza_fecha = Registro_limpieza.objects.filter(estado = "True", usuario_servicio = usuario_servicio_id, fecha = fecha_actual)
                lista_fechas = []
                for limpieza_fechas in limpieza_fecha:
                    lista_fechas.append(limpieza_fechas.limpieza_puestos.id)
                print(lista_fechas)
                return render(request, "registro_limpiezas.html", {"fecha": fecha,"limpiezas": limpieza, "puestos": puestos, "select_puesto": select_puesto, "hora_actual": hora_actual, "limpieza_fechas": limpieza_fecha, "lista_fecha": lista_fechas, "resultado_objeto": "No existe ninguna limpieza en este puesto", "mensaje_exito": "Limpieza de Puesto Registrada"})   
            else:
                return render(request, "registro_limpiezas.html", {"fecha": fecha,"limpiezas": limpieza, "puestos": puestos, "select_puesto": select_puesto, "mensaje": "No seleccionaste ninguna limpieza", "hora_actual": hora_actual, "limpieza_fechas": limpieza_fecha, "lista_fecha": lista_fechas, "resultado_objeto": "No existe ninguna limpieza en este puesto"})
        return render(request, "registro_limpiezas.html", {"fecha": fecha,"limpiezas": limpieza, "puestos": puestos, "select_puesto": select_puesto, "hora_actual": hora_actual, "limpieza_fechas": limpieza_fecha, "lista_fecha": lista_fechas, "resultado_objeto": "No existe ninguna limpieza en este puesto"})

