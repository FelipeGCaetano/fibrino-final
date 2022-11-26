from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from FibrinoDev.views import *

router = routers.DefaultRouter()
router.register('comandos', ComandosViewSet)
router.register('olt', OltViewSet)
router.register('onu', OnuViewSet)
router.register('roteador', RoteadorViewSet)
router.register('roteadorLogin', RoteadorLoginViewSet)
router.register('perfils', PerfilsViewSet)
router.register('usuarios', UsuariosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

