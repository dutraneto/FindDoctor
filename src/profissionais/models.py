from django.db import models
from django.conf import settings
from django.utils import timezone

from pessoas.models import Pessoa
from especialidades.models import Especialidade
from estabelecimentos.models import Estabelecimento

class Profissional(models.Model):
    pessoa = models.OneToOneField(Pessoa, related_name='medico', verbose_name='Profissional')
    profissao = models.CharField(verbose_name='Profissão', max_length=80, default='Médico')
    especialidade = models.ManyToManyField(Especialidade)
    # nome = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    # sobrenome = models.ForeignKey(Pessoa, verbose_name='Sobrenome', max_length=80)
    crm = models.CharField(verbose_name='CRM', max_length=10)
    estabelecimento = models.ManyToManyField(Estabelecimento, verbose_name="Locais de Atendimento")


    # foto = models.ImageField(
    #     upload_to='profissionais/images', verbose_name='Foto',
    #     null=True, blank=True)

    # created_at = models.DateTimeField('Criado em', auto_now_add=True)
    # updated_at = models.DateTimeField('Atualizado em', auto_now=True)


    @property
    def nome(self):
        self.pessoa.nome

    @property
    def sobrenome(self):
        self.pessoa.sobrenome

    def __str__(self):
        return "%s %s" % (self.pessoa.nome, self.pessoa.sobrenome)


    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering = ['pessoa']

# class Usuario(Pessoa):
#
#     nome_usuario = models.CharField(verbose_name="Usuário", max_length=30, default="")
#     email = models.EmailField(verbose_name="E-mail", max_length=80)
#     telefone_1 = models.CharField(verbose_name="Telefone Residencial", max_length=11, blank=True)
#     telefone_2 = models.CharField(verbose_name="Celular", max_length=11, blank=True)
#
#     def __str__(self):
#         return "%s %s" % (self.nome, self.sobrenome)
#
#     class Meta:
#         verbose_name = 'Usuário'
#         verbose_name_plural = 'Usuários'
#         ordering = ['nome']
