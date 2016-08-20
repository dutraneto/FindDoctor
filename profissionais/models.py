from django.db import models
from django.conf import settings
from django.utils import timezone

from pessoas.models import Pessoa
from especialidades.models import Especialidade
from estabelecimentos.models import Local
from areas.models import Area



class Profissional(Pessoa):
    especialidade = models.ManyToManyField(Especialidade)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    codConselho= models.CharField(verbose_name='Codigo do Conselho', max_length=10)
    local = models.ManyToManyField(Local, verbose_name='Local de Atendimento')

    urlImgProfissional = models.ImageField(
        upload_to='profissionais/images', verbose_name='Imagem',
        null=True, blank=True
    )







    def __str__(self):
        return "%s %s" % (self.nome, self.sobrenome)


    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering = ['nome', 'sobrenome']
