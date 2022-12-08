from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from FibrinoDev.views import *
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('comandos', ComandosViewSet)
router.register('olt', OltViewSet)
router.register('onu', OnuViewSet)
router.register('roteador', RoteadorViewSet)
router.register('roteadorLogin', RoteadorLoginViewSet)
router.register('perfis', PerfisViewSet)
router.register('usuarios', UsuariosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


