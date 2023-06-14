from django.db import models

# Create your models here.
class Visitante(models.Model):
    nome = models.TextField("Tipo", max_length=20, default="Não Especificado")
    cpf = models.TextField("Tipo", max_length=20, default="Não Especificado")
    telefone = models.TextField("Tipo", max_length=20, default="Não Especificado")

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        ordering =['id']

    def __str__(self):
        return self.nome, self.cpf, self.telefone

