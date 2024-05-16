from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User



class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Dirección")

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name} ({self.user.email})"



class MaestroProducto(models.Model):
    idp = models.IntegerField(primary_key=True)
    nomprod = models.CharField(max_length=100)
    descprod = models.CharField(max_length=300)
    precio = models.IntegerField()
    foto_prod=models.ImageField(upload_to="imagenes", default="prod.jpg", null=False, blank=False, verbose_name="Imagen")
    
    def __str__(self):
        return f'{self.idp}'
