from django.shortcuts import render, redirect
from parametros.models import Puestos, Limpieza_puestos, Registro_objetos
from login.models import Cargo_usuarios, Usuarios

# Create your views here.
def eliminar(objeto):
    objeto.estado = "False"
    objeto.save()

def eliminar_cargo(objeto):
    sin_cargo = Cargo_usuarios.objects.filter(nombre_cargo = "SIN CARGO").first()
    perfiles = Usuarios.objects.filter(cargo = objeto.id)
    for perfil in perfiles:
        perfil.cargo_id = sin_cargo.id
        perfil.save()
    objeto.estado = "False"
    objeto.save()

def eliminar_puesto(puesto):
    sin_puesto = Puestos.objects.filter(nombre_puesto = "SIN PUESTO").first()
    objetos = Registro_objetos.objects.filter(puesto = puesto.id)
    limpiezas = Limpieza_puestos.objects.filter(puesto = puesto.id)
    for objeto in objetos:
        objeto.puesto_id = sin_puesto.id
        objeto.save()
    for limpieza in limpiezas:
        limpieza.puesto_id = sin_puesto.id
        limpieza.save()
    puesto.estado = "False"
    puesto.save()

def fuera_servicio(objeto):
    objeto.servicio = "Fuera de servicio"
    objeto.save()

def operativo(objeto):
    objeto.servicio = "Operativo"
    objeto.save()
    


def edit_limpieza(request, id_limpieza):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    limpieza_edit = Limpieza_puestos.objects.filter(id = id_limpieza, estado = "True", usuario_servicio = usuario_servicio_id).first()
    print(limpieza_edit.horario_limpieza)
    if request.method == "POST":
        nombre_limpie = request.POST.get("nombre_limpie")
        hora = request.POST.get("hora")
        puesto = request.POST.get("puesto") 
        nombre = nombre_limpie.upper()
        usuario_servicio_id = request.session.get("usuario_id")
        limpie_existe = Limpieza_puestos.objects.filter(usuario_servicio = usuario_servicio_id).exclude(nombre_limpieza = limpieza_edit.nombre_limpieza, estado = "True").exclude(estado = "False") 
        nombre_existen = []
        for limpie in limpie_existe:
            nombre_existen.append(limpie.nombre_limpieza)
            print(f"nombre: {limpie.nombre_limpieza}")
        if len(nombre_limpie) < 30:   
            if hora != "":
                if puesto != "":
                    if nombre not in nombre_existen:    
                        limpieza_edit.nombre_limpieza = nombre
                        limpieza_edit.puesto_id = puesto
                        limpieza_edit.horario_limpieza = hora
                        limpieza_edit.save()
                        return redirect("limpie_puesto")
                    else:
                        return render(request, "edit_limpieza.html", {"mensaje": "Ese nombre ya esta ocupado usa otro", "puestos": puestos, "limpieza_edit": limpieza_edit})
                else:
                    return render(request, "edit_limpieza.html", {"mensaje": "No seleccionaste un puesto", "puestos": puestos, "limpieza_edit": limpieza_edit})
            else:
                return render(request, "edit_limpieza.html", {"puestos": puestos,"mensaje": "Seleccione la hora", "limpieza_edit": limpieza_edit})
        else:
            return render(request, "edit_limpieza.html", {"puestos": puestos,"mensaje": "el nombre de la limpieza no puede superarlos 25 caracteres", "limpieza_edit": limpieza_edit})
    return render(request, "edit_limpieza.html", {"puestos": puestos, "limpieza_edit": limpieza_edit})

def delet_limpieza(request, id_limpieza):
    eliminar_limpieza = Limpieza_puestos.objects.filter(id = id_limpieza).first()
    eliminar(eliminar_limpieza)
    return redirect("limpie_puesto")

def edit_freidora(request, id_freidora):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    freidora_edit = Registro_objetos.objects.filter(id = id_freidora, estado = "True", usuario_servicio = usuario_servicio_id).first()
    if request.method == "POST":
        nombre = request.POST.get("nombre_freidora")
        puesto_id = request.POST.get("puesto_id")
        nombre_freidora = nombre.upper()
        freidora_existe = Registro_objetos.objects.filter(tipo_objeto = "Freidora", usuario_servicio = usuario_servicio_id).exclude(nombre_objeto = freidora_edit.nombre_objeto, estado = "True", servicio = "Operativo").exclude(servicio = "Fuera de servicio").exclude(estado = "False")
        nombre_existen = []
        for freidora in freidora_existe:
            nombre_existen.append(freidora.nombre_objeto)
        if len(nombre_freidora) < 20:
            if puesto_id != "":   
                if nombre_freidora not in nombre_existen:    
                    freidora_edit.nombre_objeto = nombre_freidora
                    freidora_edit.puesto_id = puesto_id
                    freidora_edit.save()
                    return redirect("segui_aceite")
                else:
                    return render(request, "edit_freidora.html", {"puestos": puestos, "mensaje": "Ese nombre ya esta ocupado usa otro", "freidora_edit": freidora_edit})
            else:
                return render(request, "edit_freidora.html", {"puestos": puestos, "mensaje": "No seleccionaste un puesto", "freidora_edit": freidora_edit})
        else:
            return render(request, "edit_freidora.html", {"puestos": puestos, "mensaje": "el nombre de la freidora no puede superarlos 20 caracteres", "freidora_edit": freidora_edit})
    return render(request, "edit_freidora.html", {"puestos": puestos, "freidora_edit": freidora_edit})

def reparar_freidora(request, id_freidora):
    freidora_reparar = Registro_objetos.objects.filter(id = id_freidora).first()
    fuera_servicio(freidora_reparar)
    return redirect("segui_aceite")

def operativo_freidora(request, id_freidora):
    freidora_operativa = Registro_objetos.objects.filter(id = id_freidora).first()
    operativo(freidora_operativa)
    return redirect("segui_aceite")

def delet_freidora(request, id_freidora):
    eliminar_freidora = Registro_objetos.objects.filter(id = id_freidora).first()
    eliminar(eliminar_freidora)
    return redirect("segui_aceite")

def edit_nevera(request, id_nevera):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    puestos = Puestos.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    nevera_edit = Registro_objetos.objects.filter(id = id_nevera, estado = "True", usuario_servicio = usuario_servicio_id).first()
    if request.method == "POST":
        nombre = request.POST.get("nombre_nevera")
        puesto_id = request.POST.get("puesto_id")
        nombre_nevera = nombre.upper()
        nevera_existe = Registro_objetos.objects.filter(tipo_objeto = "Nevera", usuario_servicio = usuario_servicio_id).exclude(nombre_objeto = nevera_edit.nombre_objeto, estado = "True", servicio = "Operativo").exclude(servicio = "Fuera de servicio").exclude(estado = "False") 
        nombre_existen = []
        for nevera in nevera_existe:
            nombre_existen.append(nevera.nombre_objeto)
            print(nevera.nombre_objeto)
        if len(nombre_nevera) < 20:   
            if puesto_id != "":
                if nombre_nevera not in nombre_existen:    
                    nevera_edit.nombre_objeto = nombre_nevera
                    nevera_edit.puesto_id = puesto_id
                    nevera_edit.save()
                    return redirect("tempe_neveras")
                else:
                    return render(request, "edit_nevera.html", {"puestos": puestos, "mensaje": "Ese nombre ya esta ocupado usa otro", "nevera_edit": nevera_edit})
            else: 
                return render(request, "edit_nevera.html", {"puestos": puestos, "mensaje": "No seleccionaste un puesto", "nevera_edit": nevera_edit})   
        else:
            return render(request, "edit_nevera.html", {"puestos": puestos, "mensaje": "el nombre de la nevera no puede superarlos 20 caracteres", "nevera_edit": nevera_edit})
    
    return render(request, "edit_nevera.html", {"puestos": puestos, "nevera_edit": nevera_edit})

def reparar_nevera(request, id_nevera):
    nevera_reparar = Registro_objetos.objects.filter(id = id_nevera).first()
    fuera_servicio(nevera_reparar)
    return redirect("tempe_neveras")

def operativo_nevera(request, id_nevera):
    nevera_operativa = Registro_objetos.objects.filter(id = id_nevera).first()
    operativo(nevera_operativa)
    return redirect("tempe_neveras")

def delet_nevera(request, id_nevera):
    eliminar_nevera = Registro_objetos.objects.filter(id = id_nevera).first()
    eliminar(eliminar_nevera)
    return redirect("tempe_neveras")

def edit_puesto(request, id_puesto):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    puesto_edit = Puestos.objects.filter(id = id_puesto, estado = "True", usuario_servicio = usuario_servicio_id).first()
    if request.method == "POST":
        nombre = request.POST.get("nombre_puesto")
        nombre_puesto = nombre.upper()
        puesto_existe = Puestos.objects.filter(usuario_servicio = usuario_servicio_id).exclude(nombre_puesto = puesto_edit.nombre_puesto, estado = "True").exclude(estado = "False")
        nombre_existen = []
        for puesto in puesto_existe:
            nombre_existen.append(puesto.nombre_puesto)
            print(f"puesto: {puesto.nombre_puesto}, estado: {puesto.estado}")
        if len(nombre_puesto) < 20:   
            if nombre_puesto not in nombre_existen:    
                puesto_edit.nombre_puesto = nombre_puesto
                puesto_edit.save()
                return redirect("puestos")
            else:
                return render(request, "edit_puesto.html", {"mensaje": "Ese nombre ya esta ocupado usa otro", "puesto_edit": puesto_edit})
        else:
            return render(request, "edit_puesto.html", {"mensaje": "el nombre de la freidora no puede superarlos 20 caracteres", "puesto_edit": puesto_edit})
    return render(request, "edit_puesto.html", {"puesto_edit": puesto_edit})

def delet_puesto(request, id_puesto):
    eliminar = Puestos.objects.filter(id = id_puesto).first()
    eliminar_puesto(eliminar)
    return redirect("puestos")

def edit_cargo(request, id_cargo):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    cargo_edit = Cargo_usuarios.objects.filter(id = id_cargo, estado = "True", usuario_servicio = usuario_servicio_id).first() 
    if request.method == "POST":
        nombre = request.POST.get("nombre_cargo")
        permiso_cargo = request.POST.get("permiso") 
        nombre_cargo = nombre.upper()
        cargo_existe = Cargo_usuarios.objects.filter(usuario_servicio = usuario_servicio_id).exclude(nombre_cargo = cargo_edit.nombre_cargo, estado = "True").exclude(estado = "False")
        nombre_existen = []
        for cargo in cargo_existe:
            nombre_existen.append(cargo.nombre_cargo)
            print(f"cargo: {cargo.nombre_cargo}, estado: {cargo.estado}")
        if len(nombre_cargo) < 25:   
            if nombre_cargo not in nombre_existen:    
                cargo_edit.nombre_cargo = nombre_cargo
                cargo_edit.permiso = permiso_cargo
                cargo_edit.save()
                return redirect("cargos")
            else:
                return render(request, "edit_cargo.html", {"mensaje": "Ese nombre ya esta ocupado usa otro", "cargo_edit": cargo_edit})
        else:
            return render(request, "edit_cargo.html", {"mensaje": "el nombre del cargo no puede superarlos 25 caracteres", "cargo_edit": cargo_edit})
    return render(request, "edit_cargo.html", {"cargo_edit": cargo_edit})

def delet_cargo(request, id_cargo):
    eliminar = Cargo_usuarios.objects.filter(id = id_cargo).first()
    eliminar_cargo(eliminar)
    return redirect("cargos")

def edit_perfil(request, id_perfil):
    sesion = request.session.get("permiso_parametro")
    if sesion == False:
        return redirect("inicio")
    usuario_servicio_id = request.session.get("usuario_id")
    cargo_perfil = Cargo_usuarios.objects.filter(usuario_servicio = usuario_servicio_id, estado = "True")
    perfil_edit = Usuarios.objects.filter(id = id_perfil, estado = "True", usuario_servicio = usuario_servicio_id).first()
    if request.method == "POST":
        cargo_select = request.POST.get("cargo")
        nombre = request.POST.get("nombre")
        password = request.POST.get("password")
        repetir_password = request.POST.get("repetir_password")
        nombre_perfil = nombre.upper()
        perfil_existe = Usuarios.objects.filter(usuario_servicio = usuario_servicio_id).exclude(nombre = perfil_edit.nombre, estado = "True").exclude(estado = "False")
        nombre_existen = []
        for perfil in perfil_existe:
            nombre_existen.append(perfil.nombre)
            print(f"nombre: {perfil.nombre}, estado: {perfil.estado}")
        if password == repetir_password:
            if len(nombre) < 20:
                if cargo_select != "":
                    if nombre_perfil not in nombre_existen:
                        request.session["cargo_perfil"] = cargo_select
                        request.session["name_perfil"] = nombre_perfil
                        perfil_edit.nombre = nombre_perfil
                        perfil_edit.contraseña = password
                        perfil_edit.cargo_id = cargo_select
                        perfil_edit.save()
                        return redirect("perfil")
                    else:
                        return render(request, "edit_perfil.html", {"perfil_edit": perfil_edit,"cargo_perfil": cargo_perfil,"mensaje": "Ese nombre ya esta ocupado usa otro"})
                else:
                    return render(request, "edit_perfil.html", {"perfil_edit": perfil_edit,"cargo_perfil": cargo_perfil,"mensaje": "No seleccionaste un cargo"})
            else:
                return render(request, "edit_perfil.html", {"perfil_edit": perfil_edit,"cargo_perfil": cargo_perfil,"mensaje": "el perfil no puede superar los 20 caracteres"})
        else:
            return render(request, "edit_perfil.html", {"perfil_edit": perfil_edit,"cargo_perfil": cargo_perfil,"mensaje": "las contraseñas no son iguales"})
    else:
        return render(request, "edit_perfil.html", {"perfil_edit": perfil_edit,"cargo_perfil": cargo_perfil})

def delet_perfil(request, id_perfil):
    eliminar_perfil = Usuarios.objects.filter(id = id_perfil).first()
    eliminar(eliminar_perfil)
    return redirect("perfil")