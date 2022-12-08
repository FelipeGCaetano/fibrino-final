from rest_framework import serializers
from FibrinoDev.models import *


class ComandosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comandos
        fields = '__all__'

class OnuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onu
        fields = '__all__'
        
class RoteadorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Roteador
        fields = '__all__'

class RoteadorLoginSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = RoteadorLogin
        fields = ['nome', 'ip']
    
class OltSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olt
        fields = '__all__'
        
class PerfisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfis
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
    

        


