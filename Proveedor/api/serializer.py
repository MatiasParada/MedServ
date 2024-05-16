from rest_framework import serializers
from .models import MaestroProducto

class MaestroProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model=MaestroProducto
        fields='__all__'