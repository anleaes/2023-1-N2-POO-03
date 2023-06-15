from django.db import models

# Create your models here.
class Servicos(models.Model):
    #quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    tipo = models.TextField("Tipo", max_length=20, default="Não Especificado")
    preco = models.FloatField("Preço", default=0)


    class Meta:
        verbose_name = 'Servicos'
        verbose_name_plural = 'Servicos'
        ordering =['id']

    def __str__(self):
        #return self.quarto, self.tipo, self.preco
        return self.tipo, self.preco