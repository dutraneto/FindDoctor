from django.db import models
from areas.models import Area



class Especialidade(models.Model):

    nomeEspecialidade = models.CharField(verbose_name='Especialidade', max_length=80)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.nomeEspecialidade

    class Meta:
        ordering = ['nomeEspecialidade']
