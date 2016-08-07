from django.db import models
from profissionais.models import Profissional
# Create your models here.

class Propaganda(models.Model):
	profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
	ordem = models.IntegerField(verbose_name='Ordem')
	ativa = models.BooleanField(verbose_name='Prop. Ativa')
	urlImgPropaganda = models.ImageField(upload_to='propagandas/images', verbose_name='Numero', max_length=80, null=True, blank=True)


	def  __str__(self):
		return str(self.ordem) + " " + str(self.urlImgPropaganda)
