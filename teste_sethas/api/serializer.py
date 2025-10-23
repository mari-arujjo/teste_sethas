from rest_framework import serializers
from .models import Consumidor

class ConsumidorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Consumidor
        fields = '__all__'