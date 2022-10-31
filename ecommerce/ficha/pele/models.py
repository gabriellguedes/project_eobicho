from django.db import models

class Pele(models.Model):
	tipo_pele = models.CharField('Tipos de pele', max_length=100)
	
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.tipo_pele

class Ectoparasitas(models.Model):
	ectoparasitas = models.CharField('Ectoparasitas',  max_length=100)

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.ectoparasitas

class Infec_pele(models.Model):
	peleInfeccionada = models.CharField('Doenças na Pele', max_length=100)
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.peleInfeccionada