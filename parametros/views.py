from django.shortcuts import render, redirect
from login.models import Usuarios, Cargo_usuarios
from .models import Registro_objetos, Puestos, Limpieza_puestos

# Create your views here.
def salir_parametros(request):
    request.session["permiso_parametro"] = False
    return redirect("inicio")


    
def parametros_home(request):
    empresa = request.session.get("empresa")
    permiso = request.session.get("permiso_parametro")
    if permiso == True:
        return render(request, "home_paramet.html", {"empresa": empresa})
    else:
        return redirect("inicio")




def login_paramet(request):
    nombre = request.session.get("name_perfil")
    if request.method == "POST":
        password = request.POST.get("password")
        usuario_servicio_id = request.session.get("usuario_id")
        comprobar = Usuarios.objects.filter(nombre = nombre, contraseña = password, estado = "True", usuario_servicio = usuario_servicio_id).first()
        
        if comprobar is not None:
            request.session["permiso_parametro"] = True
            return redirect("home_parametros")
        else:
            return render(request, "login_paramet.html", {"nombre_perfil": nombre, "mensaje": "contraseña invalida"})     
    else:
        return render(request, "login_paramet.html", {"nombre_perfil": nombre})
    
def tempe_neveras(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    neveras = Registro_objetos.objects.filter(tipo_objeto="Nevera", estado = "True", usuario_servicio = usuario_servicio_id, servicio = "Operativo")
    neveras_reparar = Registro_objetos.objects.filter(tipo_objeto="Nevera", estado = "True", usuario_servicio = usuario_servicio_id, servicio = "Fuera de servicio")
    return render(request, "tempe_neveras/tempe_neveras.html", {"neveras": neveras, "neveras_reparar": neveras_reparar})

def registro_nevera(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    if request.method == "POST":
        nombre = request.POST.get("nombre_nevera")
        puesto_id = request.POST.get("puesto_id")
        nombre_nevera = nombre.upper()
        nevera_existe = Registro_objetos.objects.filter(nombre_objeto = nombre_nevera, tipo_objeto = "Nevera", usuario_servicio = usuario_servicio_id, estado = "True").first() 
        if len(nombre_nevera) < 20: 
            if puesto_id != "":  
                if nevera_existe is None:    
                    nevera = Registro_objetos(nombre_objeto=nombre_nevera, puesto_id=puesto_id, tipo_objeto = "Nevera", servicio="Operativo", estado="True", usuario_servicio_id = usuario_servicio_id)
                    nevera.save()
                    return redirect("tempe_neveras")
                else:
                    return render(request, "tempe_neveras/registro_nevera.html", {"puestos": puestos, "mensaje": "Ese nombre ya esta ocupado usa otro"})
            else:
                return render(request, "tempe_neveras/registro_nevera.html", {"puestos": puestos, "mensaje": "No seleccionaste un puesto"})
        else:
            return render(request, "tempe_neveras/registro_nevera.html", {"puestos": puestos, "mensaje": "el nombre de la nevera no puede superarlos 20 caracteres"})
    return render(request, "tempe_neveras/registro_nevera.html", {"puestos": puestos})


def segui_aceite(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    freidoras = Registro_objetos.objects.filter(tipo_objeto="Freidora", estado = "True", usuario_servicio = usuario_servicio_id, servicio = "Operativo")
    freidoras_reparar = Registro_objetos.objects.filter(tipo_objeto="Freidora", estado = "True", usuario_servicio = usuario_servicio_id, servicio = "Fuera de servicio")
    return render(request, "segui_aceite/segui_aceite.html", {"freidoras": freidoras, "freidoras_reparar": freidoras_reparar})

def registro_freidora(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    if request.method == "POST":
        nombre = request.POST.get("nombre_freidora")
        puesto_id = request.POST.get("puesto_id")
        nombre_freidora = nombre.upper()
        freidora_existe = Registro_objetos.objects.filter(nombre_objeto = nombre_freidora, tipo_objeto = "Freidora", usuario_servicio = usuario_servicio_id, estado = "True").first() 
        if len(nombre_freidora) < 20: 
            if puesto_id != "":  
                if freidora_existe is None:    
                    freidora = Registro_objetos(nombre_objeto=nombre_freidora, puesto_id=puesto_id, tipo_objeto = "Freidora", servicio="Operativo", estado="True", usuario_servicio_id = usuario_servicio_id)
                    freidora.save()
                    return redirect("segui_aceite")
                else:
                    return render(request, "segui_aceite/registro_freidora.html", {"puestos": puestos, "mensaje": "Ese nombre ya esta ocupado usa otro"})
            else:
                return render(request, "segui_aceite/registro_freidora.html", {"puestos": puestos, "mensaje": "No seleccionaste un puesto"})
        else:
            return render(request, "segui_aceite/registro_freidora.html", {"puestos": puestos, "mensaje": "el nombre de la freidora no puede superarlos 20 caracteres"})
    return render(request, "segui_aceite/registro_freidora.html", {"puestos": puestos})

def puestos(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    return render(request, "puesto/puestos.html", {"puestos": puestos})

def registro_puesto(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    if request.method == "POST":
        nombre = request.POST.get("nombre_puesto")
        nombre_puesto = nombre.upper()
        usuario_servicio = request.session.get("usuario_id")
        puesto_existe = Puestos.objects.filter(nombre_puesto = nombre_puesto, estado = "True", usuario_servicio = usuario_servicio).first() 
        if len(nombre_puesto) < 20:   
            if puesto_existe is None:    
                puesto = Puestos(nombre_puesto=nombre_puesto, estado="True", usuario_servicio_id = usuario_servicio)
                puesto.save()
                return redirect("puestos")
            else:
                return render(request, "puesto/registro_puesto.html", {"mensaje": "Ese nombre ya esta opucado usa otro"})
        else:
            return render(request, "puesto/registro_puesto.html", {"mensaje": "el nombre de la freidora no puede superarlos 20 caracteres"})
    return render(request, "puesto/registro_puesto.html")


def cargos(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    cargos = Cargo_usuarios.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    return render(request, "cargo/cargos.html", {"cargos": cargos})

def registro_cargo(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    if request.method == "POST":
        nombre = request.POST.get("nombre_cargo")
        permiso_cargo = request.POST.get("permiso") 
        nombre_cargo = nombre.upper()
        usuario_servicio_id = request.session.get("usuario_id")
        cargo_existe = Cargo_usuarios.objects.filter(nombre_cargo = nombre_cargo, estado = "True", usuario_servicio = usuario_servicio_id).first() 
        if len(nombre_cargo) < 25:   
            if cargo_existe is None:    
                cargo = Cargo_usuarios(nombre_cargo=nombre_cargo, permiso = permiso_cargo, estado="True", usuario_servicio_id = usuario_servicio_id)
                cargo.save()
                return redirect("cargos")
            else:
                return render(request, "cargo/registro_cargo.html", {"mensaje": "Ese nombre ya esta ocupado usa otro"})
        else:
            return render(request, "cargo/registro_cargo.html", {"mensaje": "el nombre del cargo no puede superarlos 25 caracteres"})
    return render(request, "cargo/registro_cargo.html")
        

def limpie_puesto(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    limpiezas = Limpieza_puestos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    return render(request, "limpie_puesto/limpie_puesto.html", {"limpiezas": limpiezas})

def registro_limpieza(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    if request.method == "POST":
        nombre_limpie = request.POST.get("nombre_limpie")
        hora = request.POST.get("hora")
        puesto = request.POST.get("puesto") 
        nombre = nombre_limpie.upper()
        usuario_servicio_id = request.session.get("usuario_id")
        limpie_existe = Limpieza_puestos.objects.filter(nombre_limpieza = nombre, estado = "True", usuario_servicio = usuario_servicio_id).first() 
        if len(nombre_limpie) < 30:   
            if hora != "":
                if puesto != "":
                    if limpie_existe is None:    
                        limpieza = Limpieza_puestos(nombre_limpieza=nombre, puesto_id = puesto, estado="True", usuario_servicio_id = usuario_servicio_id, horario_limpieza = hora)
                        limpieza.save()
                        return redirect("limpie_puesto")
                    else:
                        return render(request, "limpie_puesto/registro_limpieza.html", {"mensaje": "Ese nombre ya esta ocupado usa otro", "puestos": puestos})
                else:
                    return render(request, "limpie_puesto/registro_limpieza.html", {"mensaje": "No seleccionaste un puesto", "puestos": puestos})
            else:
                return render(request, "limpie_puesto/registro_limpieza.html", {"puestos": puestos,"mensaje": "Seleccione la hora"})
        else:
            return render(request, "limpie_puesto/registro_limpieza.html", {"puestos": puestos,"mensaje": "el nombre del cargo no puede superarlos 30 caracteres"})
    return render(request, "limpie_puesto/registro_limpieza.html", {"puestos": puestos})

def perfil(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    perfil_uso = request.session.get("id_perfil")
    usuario_servicio_id = request.session.get("usuario_id")
    perfiles = Usuarios.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    return render(request, "perfiles/perfiles.html", {"perfiles": perfiles, "perfil_uso": perfil_uso})

def registro_perfil(request):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    cargo_perfil = Cargo_usuarios.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    if request.method == "POST":
        cargo_select = request.POST.get("cargo")
        nombre = request.POST.get("nombre")
        password = request.POST.get("password")
        repetir_password = request.POST.get("repetir_password")
        nombre_perfil = nombre.upper()
        perfil_existe = Usuarios.objects.filter(nombre = nombre_perfil, estado = "True", usuario_servicio = usuario_servicio_id).first()
        if password == repetir_password:
            if len(nombre) < 20:
                if cargo_select != "":
                    if perfil_existe is None:
                        perfil = Usuarios(nombre=nombre_perfil, contraseña = password, cargo_id = cargo_select, usuario_servicio_id = usuario_servicio_id,estado = "True")
                        perfil.save()
                        return redirect("perfil")
                    else:
                        return render(request, "perfiles/registro_perfil.html", {"cargo_perfil": cargo_perfil,"mensaje": "Ese nombre ya esta ocupado usa otro"})
                else:
                    return render(request, "perfiles/registro_perfil.html", {"cargo_perfil": cargo_perfil,"mensaje": "No seleccionaste un cargo"})
            else:
                return render(request, "perfiles/registro_perfil.html", {"cargo_perfil": cargo_perfil,"mensaje": "el nombre de perfil no puede superar los 20 caracteres"})
        else:
            return render(request, "perfiles/registro_perfil.html", {"cargo_perfil": cargo_perfil,"mensaje": "las contraseñas no son iguales"})
    else:
        return render(request, "perfiles/registro_perfil.html", {"cargo_perfil": cargo_perfil})
    

def prueba(request):
    if request.method == "POST":
        hora = request.POST.get("hora")
        print(hora)
    return render(request, "limpie_puesto/prueba.html")