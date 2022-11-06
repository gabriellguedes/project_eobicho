from django.db import models

class Pele(models.Model):
	nome = models.CharField('Tipos de pele', max_length=100)
	
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.nome

class Ectoparasitas(models.Model):
	nome = models.CharField('Ectoparasitas',  max_length=100)

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.ectoparasitas

class DoencaPele(models.Model):
	nome = models.CharField('Doenças na Pele', max_length=100)
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.nome