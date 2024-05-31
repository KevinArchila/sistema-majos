from django.shortcuts import render, redirect
import datetime
from parametros.models import Registro_objetos, Puestos
from .models import Cambio_tempe

# Create your views here.



def nevera(request):
    lista = ["barra","cocina","almacen"]
    
    if request.method == "POST":
        opcion = request.POST.get("opcion")
        
        return render(request, "cambio_tempe.html", {"lista": lista})
    return render(request, "cambio_tempe.html", {"lista": lista})

def nevera_tempe(request, id_puesto):
    sesion = request.session.get("name_perfil")
    if sesion == None:
        return redirect("perfiles")
    empresa = request.session.get("empresa")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(estado = "True", usuario_servicio = usuario_servicio_id)
    if id_puesto == "inicio":

        return render(request, "cambio_tempe.html", {"puestos": puestos, "inicio": "Seleccione un puesto", "empresa": empresa})
    else:
        select_puesto = Puestos.objects.filter(id=id_puesto, usuario_servicio = usuario_servicio_id).first()
        neveras = Registro_objetos.objects.filter(puesto = id_puesto, estado = "True", servicio = "Operativo", tipo_objeto = "Nevera", usuario_servicio = usuario_servicio_id)
        if request.method == "POST":
            nevera_select = request.POST.get("opcion")
            fecha_actual = datetime.date.today()
            tempe_actual = request.POST.get("temperatura")
            horario = request.POST.get("horario")
            perfil = request.session.get("id_perfil")
            if nevera_select is not None:
                if tempe_actual != "":
                    puesto = Registro_objetos.objects.filter(id = nevera_select).first()
                    temperatura = Cambio_tempe(temperatura = tempe_actual, fecha = fecha_actual, horario = horario, registro_objeto_id = nevera_select, usuario_id = perfil, estado = "True", puesto = puesto.puesto.nombre_puesto, usuario_servicio_id = usuario_servicio_id)
                    temperatura.save()
                    return render(request, "cambio_tempe.html", {"neveras": neveras, "puestos": puestos, "select_puesto": select_puesto, "resultado_objeto": "No existen neveras en este puesto", "empresa": empresa, "mensaje_exito": "Cambio de Temperatura Registrado"})
                else:
                    return render(request, "cambio_tempe.html", {"neveras": neveras, "puestos": puestos, "select_puesto": select_puesto, "mensaje": "Te falto ingresar la temperatura", "resultado_objeto": "No existen neveras en este puesto", "empresa": empresa})
            else:
                return render(request, "cambio_tempe.html", {"neveras": neveras, "puestos": puestos, "select_puesto": select_puesto, "mensaje": "No seleccionaste ninguna nevera", "resultado_objeto": "No existen neveras en este puesto", "empresa": empresa})
        return render(request, "cambio_tempe.html", {"neveras": neveras, "puestos": puestos, "select_puesto": select_puesto, "resultado_objeto": "No existen neveras en este puesto", "empresa": empresa})
