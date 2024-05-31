from django.shortcuts import render, redirect
from login.models import Cargo_usuarios
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.



def cerrar_sesion(request):
    request.session["name_perfil"] = None
    request.session["id_perfil"] = None
    request.session["cargo_perfil"] = None
    return redirect("perfiles")


def home(request):
    request.session["permiso_parametro"] = False
    inicio = "inicio"
    nombre = request.session.get("name_perfil")
    empresa = request.session.get("empresa")
    id_perfil = request.session.get("id_perfil")
    cargo_perfil = request.session.get("cargo_perfil")
    permisos = Cargo_usuarios.objects.filter(id=cargo_perfil).first()
    if nombre and id_perfil:
        inicio = "inicio"
        return render(request, "home.html", {"nombre": nombre, "id": id_perfil, "cargos": permisos, "inicio": inicio, "empresa": empresa})
    else:
        return redirect("perfiles")

def reporte(request):
    nombre = request.session.get("name_perfil")
    if nombre == None:
        return redirect("perfiles")
    empresa = request.session.get("empresa")
    if request.method == "POST":
        nombre = request.session.get("name_perfil")
        asunto = request.POST.get("asunto")
        mensaje = request.POST.get("mensaje")
        correo_destino = request.session.get("correo_master")

        
        template = render_to_string('email_template.html', {"nombre": nombre, "mensaje": mensaje})

        email = EmailMessage(asunto, template, settings.EMAIL_HOST_USER,[correo_destino])

        
        email.send()
        return render(request, "reporte.html", {"mensaje": "Reporte enviado exitosamente", "empresa": empresa})

    return render(request, "reporte.html", {"empresa": empresa})