from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MaestroProductoSerializer
from .models import MaestroProducto
# Create your views here.



# Combina todas la operaciones crud necesarias en una sola clase wooow
class MaestroProductoViewSet(viewsets.ModelViewSet):
    queryset = MaestroProducto.objects.all()
    serializer_class= MaestroProductoSerializer