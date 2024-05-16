from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from .views import Perfil_Usuario,home,tienda,AdministrarProducto
from .views import InicioSesion, registrar_usuario, CerrarSesion
from .views import ficha
from .poblarbd import poblar_bd

urlpatterns = [
    path('', home, name="home"),
    path('InicioSesion/', InicioSesion, name="InicioSesion"),
    path('cerrar_sesion/', CerrarSesion, name='cerrar_sesion'),
    path('registrar_usuario/', registrar_usuario, name="registrar_usuario"),
    path('tienda', tienda, name="tienda"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('administrar_productos/<action>/<id>', AdministrarProducto, name="administrar_productos"),
    path('ficha/<id>', ficha, name="ficha"),
]