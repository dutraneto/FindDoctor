from django.db import models




class Estado(models.Model):
	uf = models.CharField(verbose_name='UF', max_length=2)
	nomeEstado = models.CharField(verbose_name='Nome', max_length=80)

	def __str__(self):
		return self.nomeEstado


class Cidade(models.Model):
	nomeCidade = models.CharField(verbose_name='Nome', max_length=80)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

	def __str__(self):
		return self.nomeCidade

class Local(models.Model):
	nomeLocal = models.CharField(verbose_name='Nome', max_length=150)
	cnpj = models.BigIntegerField(verbose_name="CNPJ", blank=True, null=True)
	logradouro = models.CharField(verbose_name='Logradouro', max_length=150)
	numero = models.CharField(verbose_name='Numero', max_length=10)
	bairro = models.CharField(verbose_name='Bairro', max_length=80)
	cep = models.CharField(verbose_name='CEP', max_length=12)
	cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
	telefone = models.CharField(verbose_name='Telefone', max_length=20)

	def __str__(self):
		return self.nomeLocal

	class Meta:
		verbose_name = 'Local'
		verbose_name_plural = 'Locais'
