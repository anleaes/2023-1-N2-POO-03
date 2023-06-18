from django.db import models
from visitante.models import Visitante

# Create your models here.
class Quarto(models.Model):
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE, default=0)
    tipo = models.TextField("Tipo", max_length=20, default="Não Especificado")
    numero = models.IntegerField("Número", default=0)
    capacidade = models.IntegerField("Capacidade", default=0)

    class Meta:
        verbose_name = 'Quarto'
        verbose_name_plural = 'Quartos'
        ordering =['id']

    def __str__(self):
        return f"{self.tipo} - {self.numero} - {self.capacidade} - {self.visitante}"