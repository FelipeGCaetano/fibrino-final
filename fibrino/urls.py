from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from FibrinoDev.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('comandos', ComandosViewSet)
router.register('olt', OltViewSet)
router.register('onu', OnuViewSet)
router.register('roteador', RoteadorViewSet)
router.register('roteadorLogin', RoteadorLoginViewSet)
router.register('perfis', PerfisViewSet)
router.register('usuarios', UsuariosViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Fibrino API",
      default_version='v1',
      description="API local desenvolvida pela equipe Fibrino para o setor de suporte da empresa N-Multifibra.",
      terms_of_service="#",
      contact=openapi.Contact(email="fibrinobot@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('controle-geral/', admin.site.urls), #Django admin
    path('', include(router.urls)), #Todas urls viewset
    path('teste/', include('FibrinoDev.urls')), #Pagina html
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')), #Fake Django admin
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
