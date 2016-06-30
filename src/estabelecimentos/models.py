from django.db import models

# from profissionais.models import Profissional

class Estabelecimento(models.Model):


    estabelecimento = models.CharField(verbose_name="Clínica / Hospital", max_length=100)
    logradouro = models.CharField(verbose_name="Rua", max_length=100)
    numero = models.CharField(verbose_name="Número", max_length=10)
    bairro = models.CharField(verbose_name="Bairro", max_length=80)
    cep = models.CharField(verbose_name="CEP", max_length=9, blank=True)
    cidade = models.CharField(verbose_name="Cidade", max_length=80, default="Picos")
    ddd = models.CharField(verbose_name="DDD", max_length=3, default= "089")
    telefone_1 = models.CharField(verbose_name="Telefone Comercial", max_length=8)
    telefone_2 = models.CharField(verbose_name="Telefone Celular", max_length=9, blank=True)

    def __str__(self):
        return self.estabelecimento

    class Meta:
        ordering = ['estabelecimento']
