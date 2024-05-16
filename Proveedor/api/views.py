from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MaestroProductoSerializer
from .models import MaestroProducto
# Create your views here.


class MaestroProductoViewSet(viewsets.ModelViewSet):
    queryset = MaestroProducto.objects.all()
    serializer_class= MaestroProductoSerializer