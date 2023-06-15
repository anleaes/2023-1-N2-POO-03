# Create your views here.
from .models import Servicos
from rest_framework import viewsets
from .serializers import ServicosSerializer

class ServicosViewSet(viewsets.ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer  
