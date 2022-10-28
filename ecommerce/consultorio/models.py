from django.db import models


class Vacina(models.Model):
	nome = models.CharField('Nome', max_length=100)
	dose = models.IntegerField('Doses',)

	def __str__(self):
		return self.nome
