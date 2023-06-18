from .models import Estacionamento
from rest_framework import viewsets
from .serializers import EstacionamentoSerializer

class EstacionamentoViewSet(viewsets.ModelViewSet):
    queryset = Estacionamento.objects.all()
    serializer_class = EstacionamentoSerializer  
