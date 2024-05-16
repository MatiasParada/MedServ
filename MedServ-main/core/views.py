from django.shortcuts import render,redirect
from django. contrib.auth import login, logout, authenticate
from django. contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import  MaestroProducto,PerfilUsuario
from .forms import MaestroProductoForm,IniciarSesionForm,RegistrarUsuarioForm,PerfilUsuarioForm



def home(request):
    return render(request, 'core/home.html')

## vistas crud de sesion
def InicioSesion(request):
    data = {"mesg": "", "form": IniciarSesionForm()}

    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(home)
                else:
                    data["mesg"] = "¡La cuenta o la password no son correctos!"
            else:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
    return render(request, "core/InicioSesion.html", data)

def CerrarSesion(request):
    logout(request)
    return redirect(home)

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            rut = request.POST.get("rut")
            direccion = request.POST.get("direccion")
            PerfilUsuario.objects.update_or_create(user=user, rut=rut, direccion=direccion)
            return redirect(InicioSesion)
    form = RegistrarUsuarioForm()
    return render(request, "core/registrar_usuario.html", context={'form': form})

def Perfil_Usuario(request):
    data = {"mesg": "", "form": PerfilUsuarioForm}

    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.save()
            perfil = PerfilUsuario.objects.get(user=user)
            perfil.rut = request.POST.get("rut")
            perfil.save()
            data["mesg"] = "¡Sus datos fueron actualizados correctamente!"

    perfil = PerfilUsuario.objects.get(user=request.user)
    form = PerfilUsuarioForm()
    form.fields['first_name'].initial = request.user.first_name
    form.fields['last_name'].initial = request.user.last_name
    form.fields['email'].initial = request.user.email
    form.fields['rut'].initial = perfil.rut
    data["form"] = form
    return render(request, "core/perfil_usuario.html", data)

def tienda(request):
    data = {'list': MaestroProducto.objects.all().order_by('idp')}
    return render(request, 'core/tienda.html', data)

@csrf_exempt
def AdministrarProducto(request, action, id):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect(home)

    data = {"mesg": "", "form": MaestroProductoForm, "action": action, "id": id, "formsesion": IniciarSesionForm}

    if action == 'ins':
        if request.method == 'POST':
            form = MaestroProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data['mesg'] = "!El producto fue creado correctamente¡"
                except:
                    data['mesg'] = "!No se puede crear dos productos con el mismo identificador¡"
    
    elif action == 'upd':
        objeto = MaestroProducto.objects.get(idp=id)
        if request.method == "POST":
            form = MaestroProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El vehículo fue actualizado correctamente!"
        data["form"] = MaestroProductoForm(instance=objeto)

    elif action == 'del':
        try:
            MaestroProducto.objects.get(idp=id).delete()
            data["mesg"] = "¡El vehículo fue eliminado correctamente!"
            return redirect(AdministrarProducto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El vehículo ya estaba eliminado!"

    data["list"] = MaestroProducto.objects.all().order_by('idp')
    return render(request, "core/administrar_productos.html", data)
def ficha(request, id):
    data = {"mesg": "", "maestroproducto": None}

    if request.method == "POST":
        if request.user.is_authenticated and not request.user.is_staff:
            
            data["mesg"] = "¡Para poder comprar debe iniciar sesión como cliente!"

    data["maestroproducto"] = MaestroProducto.objects.get(idp=id)
    return render(request, "core/ficha.html", data)
