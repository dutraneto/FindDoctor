from django.db import models



class Especialidade(models.Model):

    especialidade = models.CharField(verbose_name='Especialidade', max_length=80)
    #nome_profissional = models.ManyToManyField(Profissional, related_name='Profissional')


    # created_at = models.DateTimeField('Criado em', auto_now_add=True)
    # updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.especialidade

    class Meta:
        ordering = ['especialidade']
