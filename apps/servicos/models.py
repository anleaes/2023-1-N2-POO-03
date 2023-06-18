from django.db import models
from quarto.models import Quarto

# Create your models here.
class Servicos(models.Model):
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, default=0)
    tipo = models.TextField("Tipo", max_length=20, default="Não Especificado")
    preco = models.FloatField("Preço", default=0)


    class Meta:
        verbose_name = 'Servicos'
        verbose_name_plural = 'Servicos'
        ordering =['id']

    def __str__(self):
        return self.quarto, self.tipo, self.preco
        