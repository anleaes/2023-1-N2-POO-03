from .models import Visitante
from rest_framework import viewsets
from .serializers import VisitanteSerializer

class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer  
