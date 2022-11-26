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
        fields = '__all__'
    
class OltSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olt
        fields = '__all__'
        
class PerfilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfils
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

        

    """     def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número de CPF inválido."})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "O nome não pode conter dígitos."})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 dígitos."})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O número de celular deve seguir o padrão: xx xxxxx-xxxx"})
        return data """


