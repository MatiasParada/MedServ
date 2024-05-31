from rest_framework import serializers
from .models import MaestroProducto



# Herramienta que facilita la conversión  de los modelos a json
class MaestroProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model=MaestroProducto
        fields='__all__'