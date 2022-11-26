from rest_framework import viewsets, filters
from fibrino.serializers import *
from FibrinoDev.models import *
from django_filters.rest_framework import DjangoFilterBackend

class ComandosViewSet(viewsets.ModelViewSet):
    """Listando comandos"""
    queryset = Comandos.objects.all()
    serializer_class = ComandosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['header', 'descricao']
    #filterset_fields = ['ativo']


class OnuViewSet(viewsets.ModelViewSet):
    """Listando ONU"""
    queryset = Onu.objects.all()
    serializer_class = OnuSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['marca']

class OltViewSet(viewsets.ModelViewSet):
    """Listando OLT"""
    queryset = Olt.objects.all()
    serializer_class = OltSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['nome']
    #filterset_fields = ['ativo']

class RoteadorViewSet(viewsets.ModelViewSet):
    """Listando Roteador"""
    queryset = Roteador.objects.all()
    serializer_class = RoteadorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['marca', 'modelo','transmissao','emulador']
    #filterset_fields = ['ativo']

class RoteadorLoginViewSet(viewsets.ModelViewSet):
    """Listando Login de roteadores"""
    queryset = RoteadorLogin.objects.all()
    serializer_class = RoteadorLoginSeriealizer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['roteador_id', 'usuario','senha']
    #filterset_fields = ['ativo']

class PerfilsViewSet(viewsets.ModelViewSet):
    """Listando Perfis"""
    queryset = Perfils.objects.all()
    serializer_class = PerfilsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['perfil', 'descicao']

class UsuariosViewSet(viewsets.ModelViewSet):
    """Listando Usuarios"""
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['nome', 'nome_usuario', 'senha', 'estagiario', 'efetivo', 'admin']
    