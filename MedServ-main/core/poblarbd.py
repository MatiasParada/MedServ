from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import PerfilUsuario, MaestroProducto
from .views import home,tienda

def poblar_bd(request):
    
    
    #  ----------------------------------Poblar usuarios----------------------------------
    
    
    #-----------------cliente
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
        return HttpResponse(f"Error al crear usuario cliente: {err}", status=500)
    
    #-----------------Staff
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
        return HttpResponse(f"Error al crear usuario staff: {err}", status=500)


    # ---------------------------------- Poblar productos ----------------------------------
    
    try:
        MaestroProducto.objects.all().delete()
        print("Tabla MaestroProducto fue truncada.")
    except Exception as err:
        print(f"Error al truncar la tabla MaestroProducto: {err}")
        return HttpResponse(f"Error al truncar la tabla MaestroProducto: {err}", status=500)

    try:
        ultimo_id = MaestroProducto.objects.latest('idp').idp if MaestroProducto.objects.exists() else 0
        
        productos_para_agregar = [
                {'idp': ultimo_id + 1, 'nomprod': 'Mascarillas N95', 'descprod': 'Pack de 10 unidades', 'precio': 19990, 'foto_prod': 'img/mascarilla_n95.jpg', 'stock': 4},
                {'idp': ultimo_id + 2, 'nomprod': 'Guantes de látex estériles', 'descprod': 'Caja de 100 unidades', 'precio': 4990, 'foto_prod': 'img/guantes_latex.jpg', 'stock': 7},
                {'idp': ultimo_id + 3, 'nomprod': 'Termómetro infrarrojo', 'descprod': 'Medición sin contacto', 'precio': 29990, 'foto_prod': 'img/termometro_infrarrojo.jpg', 'stock': 8},
                {'idp': ultimo_id + 4, 'nomprod': 'Alcohol en gel', 'descprod': '500 ml', 'precio': 4990, 'foto_prod': 'img/alcohol_gel.jpg', 'stock': 3},
                {'idp': ultimo_id + 5, 'nomprod': 'Batas quirúrgicas', 'descprod': 'Paquete de 5 unidades', 'precio': 8990, 'foto_prod': 'img/batas_quirurgicas.jpg', 'stock': 4},
                {'idp': ultimo_id + 6, 'nomprod': 'Respiradores médicos', 'descprod': 'Certificación NIOSH N95', 'precio': 29990, 'foto_prod': 'img/respiradores.jpg', 'stock': 4},
            ]
        print("Iniciar poblamiento de la tabla MaestroProducto.")
        for producto in productos_para_agregar:
            MaestroProducto.objects.create(**producto)

        print("Tabla MaestroProducto fue poblada.")
    except Exception as err:
        print(f"Error al poblar la tabla MaestroProducto: {err}")
        return HttpResponse(f"Error al poblar la tabla MaestroProducto: {err}", status=500)

    print(f"Base de datos poblada exitosamente.")
    return redirect(tienda)
