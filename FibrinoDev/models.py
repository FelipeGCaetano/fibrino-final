from django.db import models
from dict_funcao_comandos import FUNÇÃO, marcas

class Comandos(models.Model):
    id = models.AutoField(primary_key=True)
    dict_funcao = FUNÇÃO
    função = models.CharField(max_length=100, choices=dict_funcao, blank=False, null=False, default=' ')
    comando = models.CharField(blank=False, max_length=100)
    descricao = models.CharField(unique=True, max_length=100)


class Olt(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(blank=False, max_length=100)
    ip = models.CharField(blank=False, max_length=100, default='0.0.0.0')

class Onu(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(blank=False, max_length=100)

class Roteador(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(blank=False, choices=marcas, max_length=100)
    modelo = models.CharField(blank=False, max_length=100)
    transmissao = models.CharField(blank=False, max_length=100)
    emulador = models.CharField(blank=False, default="Não Localizado", max_length=100)
    foto = models.ImageField(blank=True, max_length=255)


class Perfis(models.Model):
    id = models.AutoField(primary_key=True)
    perfil = models.CharField(blank=False, max_length=100)
    descricao = models.CharField(blank=False, max_length=100)
    

class RoteadorLogin(models.Model):
    id = models.AutoField(primary_key=True)
    marca_roteador = models.CharField(choices=marcas, max_length=100, default=' ')
    usuario = models.CharField(blank=False, max_length=100)
    senha = models.CharField(blank=False, max_length=100)


class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(blank=False, max_length=100)
    nome_usuario = models.CharField(blank=False, max_length=100)
    senha = models.CharField(blank=False, max_length=100)
    estagiario = models.CharField(default=0, max_length=100)
    efetivo = models.CharField(default=0, max_length=100)
    admin = models.CharField(default=0, max_length=100)

def __str__(self):
    return self.nome