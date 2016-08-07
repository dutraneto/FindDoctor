# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Area(models.Model):

	nomeArea = models.CharField(verbose_name='Profissão', max_length=80)



	def __str__(self):
		return self.nomeArea
