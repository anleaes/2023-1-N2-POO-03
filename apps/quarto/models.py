from django.db import models

# Create your models here.
class Quarto(models.Model):
    
    tipo = models.TextField("Tipo", max_length=20, default="Não Especificado")
    numero = models.TextField("Número", max_length=3, default="Não Especificado")
    capacidade = models.TextField("Capacidade", max_length=2, default="Não Especificado")

    class Meta:
        verbose_name = 'Quarto'
        verbose_name_plural = 'Quartos'
        ordering =['id']

    def __str__(self):
        return self.tipo, self.numero, self.capacidade, self.visitante