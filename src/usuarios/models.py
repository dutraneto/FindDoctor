from django.db import models
from pessoas.models import (Pessoa)

class Usuario(Pessoa):

    pessoa = models.OneToOneField(Pessoa, verbose_name="Usuário", default="")
    email = models.EmailField(verbose_name="E-mail", max_length=80)
    telefone_1 = models.CharField(verbose_name="Telefone Residencial", max_length=11, blank=True)
    telefone_2 = models.CharField(verbose_name="Celular", max_length=11, blank=True)

    @property
    def nome(self):
        self.pessoa.nome

    @property
    def sobrenome(self):
        self.pessoa.sobrenome

    def __str__(self):
        return "%s %s" % (self.pessoa.nome, self.pessoa.sobrenome)


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome']
