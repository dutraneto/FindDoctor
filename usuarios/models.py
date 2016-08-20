# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from pessoas.models import (Pessoa)
from estabelecimentos.models import Estado

class Usuario(Pessoa):


    email = models.CharField(verbose_name='Email', max_length=80)
    senha = models.CharField(verbose_name='Senha', max_length=80)

    def __str__(self):
        return self.especialidade


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        #ordering = ['nome']
