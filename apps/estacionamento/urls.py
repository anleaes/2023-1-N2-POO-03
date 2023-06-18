from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'estacionamento'

router = routers.DefaultRouter()
router.register('estacionamento', views.EstacionamentoViewSet, basename='estacionamento')

urlpatterns = [
    path('', include(router.urls) )
]
