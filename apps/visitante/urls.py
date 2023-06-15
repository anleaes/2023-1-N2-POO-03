from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'visitante'

router = routers.DefaultRouter()
router.register('visitante', views.VisitanteViewSet, basename='visitante')

urlpatterns = [
    path('', include(router.urls) )
]