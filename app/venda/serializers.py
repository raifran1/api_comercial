from rest_framework import serializers
from .models import VendasProd, Venda

class VendasProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendasProd
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'