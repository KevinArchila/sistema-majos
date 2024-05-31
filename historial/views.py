from django.shortcuts import render, redirect
from freidora.models import Cambio_aceite
from nevera.models import Cambio_tempe
from limpieza.models import Registro_limpieza
from parametros.models import Registro_objetos, Limpieza_puestos
import datetime

# Create your views here.
def borrar_histori(registro):
    registro.estado = "False"
    registro.save()

def historial_home(request):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    inicio = "inicio"
    return render(request, "home_historial.html", {"inicio": inicio})

def histori_aceite(request):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    usuario_servicio_id = request.session.get("usuario_id")
    
    fecha = request.GET.get("fecha")
    if fecha is None:
        fecha_actual = datetime.date.today()
        
        registro_filtro = Cambio_aceite.objects.filter(fecha=fecha_actual, usuario_servicio = usuario_servicio_id, estado = "True")
        if registro_filtro:
            return render(request, "histori_aceites/histori_aceite.html", {"registro_filtro": registro_filtro, "fecha_input": fecha_actual})
        else:
            return render(request, "histori_aceites/histori_aceite.html", {"mensaje": "No hay registros de hoy", "fecha_input": fecha_actual})
    else:
        fecha_filtro = Cambio_aceite.objects.filter(fecha=fecha, usuario_servicio = usuario_servicio_id)
        if fecha_filtro:
            
            return render(request, "histori_aceites/histori_aceite.html", {"registro_filtro": fecha_filtro, "fecha_input_format": fecha})
        else:
            return render(request, "histori_aceites/histori_aceite.html", {"mensaje": "No existen registros en esa fecha", "fecha_input_format": fecha})

def edit_histori_aceite(request, id_registro):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    usuario_servicio_id = request.session.get("usuario_id")
    freidora_edit = Cambio_aceite.objects.filter(id = id_registro, usuario_servicio = usuario_servicio_id).first()
    freidoras = Registro_objetos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True", tipo_objeto = "Freidora")
    horarios = ["Mañana", "Tarde", "Noche"]
    if request.method == "POST":
        freidora = request.POST.get("freidora")
        horario = request.POST.get("horario")
        freidora_edit.registro_objeto_id = freidora
        freidora_edit.horario = horario
        freidora_edit.save()
        return redirect("histori_aceite")

    return render(request, "histori_aceites/edit_histori_aceite.html", {"freidora_edit": freidora_edit, "horarios": horarios, "freidoras": freidoras})

def delet_aceite(request, id_registro):
    usuario_servicio_id = request.session.get("usuario_id")
    registro_aceite = Cambio_aceite.objects.filter(id = id_registro, estado = "True", usuario_servicio = usuario_servicio_id).first()
    borrar_histori(registro_aceite)
    return redirect("histori_aceite")


def histori_tempe(request):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    usuario_servicio_id = request.session.get("usuario_id")
    
    fecha = request.GET.get("fecha")
    if fecha is None:
        fecha_actual = datetime.date.today()
        registro_filtro = Cambio_tempe.objects.filter(fecha=fecha_actual, usuario_servicio = usuario_servicio_id, estado = "True")
        if registro_filtro:
            return render(request, "histori_tempe/histori_tempe.html", {"registro_filtro": registro_filtro, "fecha_input": fecha_actual})
        else:
            return render(request, "histori_tempe/histori_tempe.html", {"mensaje": "No hay registros de hoy", "fecha_input": fecha_actual})
    else:
        fecha_filtro = Cambio_tempe.objects.filter(fecha=fecha, usuario_servicio = usuario_servicio_id, estado = "True")
        if fecha_filtro:
            
            return render(request, "histori_tempe/histori_tempe.html", {"registro_filtro": fecha_filtro, "fecha_input_format": fecha})
        else:
            return render(request, "histori_tempe/histori_tempe.html", {"mensaje": "No existen registros en esa fecha", "fecha_input_format": fecha})

def edit_histori_tempe(request, id_registro):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    usuario_servicio_id = request.session.get("usuario_id")
    nevera_edit = Cambio_tempe.objects.filter(id = id_registro, usuario_servicio = usuario_servicio_id, estado = "True").first()
    neveras = Registro_objetos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True", tipo_objeto = "Nevera")
    horarios = ["Mañana", "Tarde", "Noche"]
    if request.method == "POST":
        nevera = request.POST.get("nevera")
        horario = request.POST.get("horario")
        temperatura = request.POST.get("temperatura")
        if temperatura:
            nevera_edit.registro_objeto_id = nevera
            nevera_edit.horario = horario
            nevera_edit.temperatura = temperatura
            nevera_edit.save()
            return redirect("histori_tempe")
        else:
            return render(request, "histori_tempe/edit_histori_tempe.html", {"nevera_edit": nevera_edit, "horarios": horarios, "neveras": neveras, "mensaje": "Ingresa la temperatura"})
    return render(request, "histori_tempe/edit_histori_tempe.html", {"nevera_edit": nevera_edit, "horarios": horarios, "neveras": neveras})

def delet_tempe(request, id_registro):
    usuario_servicio_id = request.session.get("usuario_id")
    registro_tempe = Cambio_tempe.objects.filter(id = id_registro, estado = "True", usuario_servicio = usuario_servicio_id).first()
    borrar_histori(registro_tempe)
    return redirect("histori_tempe")


def histori_limpie(request):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    usuario_servicio_id = request.session.get("usuario_id")
    fecha = request.GET.get("fecha")
    if fecha is None:
        fecha_actual = datetime.date.today()
        registro_filtro = Registro_limpieza.objects.filter(fecha=fecha_actual, usuario_servicio = usuario_servicio_id, estado = "True")
        if registro_filtro:
            return render(request, "histori_limpie/histori_limpie.html", {"registro_filtro": registro_filtro, "fecha_input": fecha_actual})
        else:
            return render(request, "histori_limpie/histori_limpie.html", {"mensaje": "No hay registros de hoy", "fecha_input": fecha_actual})
    else:
        fecha_filtro = Registro_limpieza.objects.filter(fecha=fecha, usuario_servicio = usuario_servicio_id, estado = "True")
        if fecha_filtro:
            return render(request, "histori_limpie/histori_limpie.html", {"registro_filtro": fecha_filtro, "fecha_input_format": fecha})
        else:
            return render(request, "histori_limpie/histori_limpie.html", {"mensaje": "No existen registros en esa fecha", "fecha_input_format": fecha})
        
def edit_histori_limpie(request, id_registro):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    usuario_servicio_id = request.session.get("usuario_id")
    limpieza_edit = Registro_limpieza.objects.filter(id = id_registro, usuario_servicio = usuario_servicio_id, estado = "True").first()
    limpiezas = Limpieza_puestos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    horarios = ["Mañana", "Tarde", "Noche"]
    if request.method == "POST":
        horario = request.POST.get("horario")
        limpieza_edit.horario = horario
        limpieza_edit.save()
        return redirect("histori_limpie")

    return render(request, "histori_limpie/edit_histori_limpie.html", {"limpieza_edit": limpieza_edit, "horarios": horarios, "limpiezas": limpiezas})

def delet_limpie(request, id_registro):
    usuario_servicio_id = request.session.get("usuario_id")
    registro_limpie = Registro_limpieza.objects.filter(id = id_registro, estado = "True", usuario_servicio = usuario_servicio_id).first()
    borrar_histori(registro_limpie)
    return redirect("histori_limpie")