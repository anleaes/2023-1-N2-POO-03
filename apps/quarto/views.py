from django.shortcuts import render

# Create your views here.
from .models import Quarto
from rest_framework import viewsets
from .serializers import QuartoSerializer

class QuartoViewSet(viewsets.ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer  