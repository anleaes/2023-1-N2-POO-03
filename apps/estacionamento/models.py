from django.db import models
from visitante.models import Visitante

# Create your models here.
class Estacionamento(models.Model):
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE, default=0)
    vaga_codigo = models.IntegerField("Código da Vaga", default=0)
    vagas_totais = models.IntegerField("Vagas Totais", default=0)
    vagas_ocupadas = models.IntegerField("Vagas Ocupadas", default=0)

    class Meta:
        verbose_name = 'Estacionamento'
        verbose_name_plural = 'Estacionamentos'
        ordering =['id']

    def __str__(self):
        return self.vaga_codigo, self.vagas_totais, self.vagas_ocupadas
