from .models import Visitante
from rest_framework import serializers

class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']
