from operator import index
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import PerfilUsuario, MaestroProducto
from .views import home, AdministrarProducto

def poblar_bd(request):
    try:
        print("Verificar si existe usuario cliente.")
        if User.objects.filter(username="usuario_cliente").exists():
            print("Intentando eliminar usuario cliente.")
            User.objects.get(username="usuario_cliente").delete()
            print("Usuario cliente eliminado.")
        print("Iniciando creación de usuario cliente.")
        user = User.objects.create_user(username="usuario_cliente", password='Duoc@123')
        user.first_name = "Chris"
        user.last_name = "Evans (Cliente)"
        user.email = "cevans@marvel.com"
        user.is_superuser = False
        user.is_staff = False
        PerfilUsuario.objects.create(user=user, rut="11.111.111-K", direccion="Burbank (Estados Unidos)")
        user.save()
        print("Usuario cliente fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario cliente: {err}")
    try:
        print("Verificar si existe usuario staff.")
        if User.objects.filter(username="usuario_staff").exists():
            print("Intentando eliminar usuario staff.")
            User.objects.get(username="usuario_staff").delete()
            print("Usuario staff eliminado.")
        print("Iniciando creación de usuario staff.")
        user = User.objects.create_user(username="usuario_staff", password='Duoc@123')
        user.first_name = "Pepper"
        user.last_name = "Potts (Staff)"
        user.email = "ppotts@tiendastark.com"
        user.is_superuser = True
        user.is_staff = True
        PerfilUsuario.objects.create(user=user, rut="22.222.222-K", direccion="Burbank (Estados Unidos)")
        user.save()
        print("Usuario staff fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario staff: {err}")
    try:
        MaestroProducto.objects.all().delete()
        print("Tabla Vehiculo fue truncada.")
    except Exception as err:
        print(f"Error al poblar tabla Categoria: {err}")        
        
    try:
        print("Iniciar poblamiento de tabla Vehiculo.")
        MaestroProducto.objects.create(idp=1, nomprod='Mascarillas N95', descprod="Pack de 10 unidades", precio=19990, foto_prod="img/mascarilla_n95.jpg"),
        MaestroProducto.objects.create(idp=2, nomprod='Guantes de látex estériles', descprod="Caja de 100 unidades", precio=4990, foto_prod="img/guantes_latex.jpg"),
        MaestroProducto.objects.create(idp=3, nomprod='Termómetro infrarrojo', descprod="Medición sin contacto", precio=29990, foto_prod="img/termometro_infrarrojo.jpg"),
        MaestroProducto.objects.create(idp=4, nomprod='Alcohol en gel', descprod="500 ml", precio=4990, foto_prod="img/alcohol_gel.jpg"),
        MaestroProducto.objects.create(idp=5, nomprod='Batas quirúrgicas', descprod="Paquete de 5 unidades", precio=8990, foto_prod="img/batas_quirurgicas.jpg"),
        MaestroProducto.objects.create(idp=6, nomprod='Respiradores médicos', descprod="Certificación NIOSH N95", precio=29990, foto_prod="img/respiradores.jpg"),

        print("Tabla Vehiculo fue poblada.")
    except Exception as err:
        print(f"Error al poblar vehículos: {err}")
        return redirect(home)


