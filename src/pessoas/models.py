from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=80)
    sobrenome = models.CharField(verbose_name="Sobrenome", max_length=80)

    def __str__(self):
        return "%s %s" % (self.nome, self.sobrenome)
