from django.urls import path,include
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from api import views



router=routers.DefaultRouter()
router.register(r'Productos',views.MaestroProductoViewSet)

urlpatterns=[
    path('', include(router.urls))
    ]