from django.db import models

class Patas(models.Model):
	nome = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return self.nome