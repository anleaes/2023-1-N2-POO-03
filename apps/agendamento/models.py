from django.db import models

# Create your models here.
class Agendamento(models.Model):
    #visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    #quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_entrada = models.DateTimeField("Data Entrada")
    data_saida = models.DateTimeField("Data Saída")


    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering =['id']

    def __str__(self):
        #return self.visitante, self.quarto, self.data_entrada, self.data_saida
        return self.data_entrada, self.data_saida