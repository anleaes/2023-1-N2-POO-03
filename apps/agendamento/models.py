from django.db import models
from visitante.models import Visitante
from quarto.models import Quarto

# Create your models here.
class Agendamento(models.Model):
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE, default=0)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, default=0)
    data_entrada = models.DateTimeField("Data Entrada")
    data_saida = models.DateTimeField("Data Saída")


    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering =['id']

    def __str__(self):
        return self.visitante, self.quarto, self.data_entrada, self.data_saida
        