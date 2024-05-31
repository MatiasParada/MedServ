from django.http import JsonResponse
from .models import  MaestroProducto
from django.shortcuts import redirect 
import requests
import os
from django.conf import settings






#-----------------llamar los productos por id
def obtener_producto_por_id(id_producto):
    url = f"http://127.0.0.1:4000/api/v1/Productos/{id_producto}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        producto = response.json()
        return producto
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el producto: {e}")
        return None


#----------------- lista de ids para que no se repitan
id_agregados = []



#----------------- agregar producto a nuestra BD

def agregar_producto(request, id_producto):
    # Verificar si el producto ya está en la lista de IDs agregados
    if id_producto in id_agregados:
        print(f"El producto con ID {id_producto} ya fue agregado.")
        return redirect('proveedor')

    
    producto = obtener_producto_por_id(id_producto)
    if not producto:
        # Manejar el caso en que el producto no se encuentra
        print(f"El producto con ID {id_producto} no se encontró.")
        return redirect('proveedor')

    try:
        ultimo_id = MaestroProducto.objects.latest('idp').idp
    except MaestroProducto.DoesNotExist:
        ultimo_id = 0
    
    # Crea un producto
    nuevo_producto = MaestroProducto.objects.create(
        idp=ultimo_id + 1,
        nomprod=producto['nomprod'],
        descprod=producto['descprod'],
        precio=producto['precio'],
        stock=producto['stock']
    )

    # Agrega la id a la lista
    id_agregados.append(id_producto)
    
    # Descargar la imagen del producto y guardarla 
    imagen_url = producto['foto_prod']
    imagen_nombre = os.path.basename(imagen_url)
    imagen_ruta = os.path.join(settings.MEDIA_ROOT, 'img', imagen_nombre)
    
    try:
        imagen_respuesta = requests.get(imagen_url)
        imagen_respuesta.raise_for_status()
        with open(imagen_ruta, 'wb') as imagen_archivo:
            imagen_archivo.write(imagen_respuesta.content)
        
        # Guardar la ruta de la imagen en el producto
        nuevo_producto.foto_prod = os.path.join('img', imagen_nombre)
        nuevo_producto.save()
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
    
    # Depuración para ver los ids
    print("IDs agregados:", id_agregados)
    
    return redirect('proveedor')