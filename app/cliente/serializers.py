from rest_framework import serializers
from .models import Cliente, Endereco

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        # fields = ['campo1', 'campo2' ...]
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'