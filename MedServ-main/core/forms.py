from django import forms
from django.forms import ModelForm, fields, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import MaestroProducto


class IniciarSesionForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Correo")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class RegistrarUsuarioForm(UserCreationForm):
    rut = forms.CharField(max_length=80, required=True, label="Rut")
    direccion = forms.CharField(max_length=80, required=True, label="Direccion")
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','rut','direccion']

class PerfilUsuarioForm(Form):
    first_name = forms.CharField(max_length=150, required=True, label="Nombres") 
    last_name = forms.CharField(max_length=150, required=True, label="Apellidos")
    email = forms.CharField(max_length=260, required=True, label="Correo")
    rut = forms.CharField(max_length=80, required=False, label="Rut")
    
    class Meta:
        fields = '__all__'


        
class MaestroProductoForm(ModelForm):
        class Meta:
            model = MaestroProducto
            fields = ['idp', 'nomprod', 'descprod', 'precio','foto_prod']
