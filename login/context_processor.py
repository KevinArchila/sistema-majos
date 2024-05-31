from .models import Cargo_usuarios

def cargos(request):
    cargos = Cargo_usuarios.objects.all()
    return {'cargos': cargos}

def nombre_empresa(request):
    empresa = request.session.get("empresa")
    return {"empresa": empresa}
