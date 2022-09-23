from django.db import models
from ecommerce.pet.tuplas import Tuplas
from ecommerce.pet.models import Pet
from django.contrib.auth.models import User
from ecommerce.core.models import TimeStampedModel

t = Tuplas()

class Prontuario(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
    	return '{} - {}'.format(self.pk, self.created.strftime('%d-%m-%Y'))

class Doenca(models.Model):
	doenca = models.CharField(max_length=150)
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.doenca)

class Pele(models.Model):
	tipo_pele = models.CharField('Outros', max_length=100)
	
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.tipo_pele)		

class Ectoparasitas(models.Model):
	ectoparasitas = models.CharField('Ectoparasitas',  max_length=100)

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.ectoparasitas)	

class Infec_pele(models.Model):
	peleInfeccionada = models.CharField('Infecção na Pele', max_length=100)
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.peleInfeccionada)		

class Pelos(models.Model):
	pelos = models.CharField('Pelos', max_length=100)

	class Meta:
		ordering =('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.pelos)

class Estado_pelos(models.Model):	
	pelosEstado = models.CharField('Estado do Pelo', max_length=100)
	class Meta:
		ordering =('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.pelosEstado)

class Condicao_pelos(models.Model):
	pelosCondicao = models.CharField('Condição dos Pelos', max_length=100)
	class Meta:
		ordering =('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.pelosCondicao)

class Ficha(models.Model):
	prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, default=None)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='fichaPets')
	pele = models.ForeignKey(Pele, on_delete=models.CASCADE, default=None)
	pelos = models.ForeignKey(Pelos, on_delete=models.CASCADE, default=None)
	obs = models.TextField('', max_length=400, blank=True, null=True)
	

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.pet.pk)

""" 
unhas = models.CharField('', max_length=100, choices=t.UNHAS_CHOICES)
	boca = models.CharField('', max_length=100, choices=t.BOCA_CHOICES)
	olhos = models.CharField('', max_length=100, choices=t.OLHOS_CHOICES)
	patas = models.CharField('', max_length=100, choices=t.PATAS_CHOICES)
	orelhas = models.CharField('', max_length=100, choices=t.ORELHAS_CHOICES)
	doenca = models.CharField('', max_length=100, choices=t.DOENCA_CHOICES)
"""