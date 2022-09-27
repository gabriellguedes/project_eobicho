from django.db import models
from ecommerce.pet.tuplas import Tuplas
from ecommerce.pet.models import Pet
from django.contrib.auth.models import User
from ecommerce.core.models import TimeStampedModel

t = Tuplas()

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

class Boca(models.Model):
	boca = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return '{} - {}'.format(self.pk, self.boca)	

class Unhas(models.Model):
	unhas = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return '{} - {}'.format(self.pk, self.unhas)

class Olhos(models.Model):
	olhos = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return '{}-{}'.format(self.pk, self.olhos)
class Patas(models.Model):
	patas = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return '{} - {}'.format(self.pk, self.patas)

class Orelhas(models.Model):
	orelhas = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	
	def __str__(self):
		return '{} - {}'.format(self.pk, self.orelhas)

class Ficha(models.Model):
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='fichaPets')
	pele = models.ForeignKey(Pele, on_delete=models.CASCADE)
	peleInfeccionada = models.ForeignKey(Infec_pele, on_delete=models.CASCADE)
	pelos = models.ForeignKey(Pelos, on_delete=models.CASCADE)
	pelosEstado = models.ForeignKey(Estado_pelos, on_delete=models.CASCADE)
	pelosCondicao = models.ForeignKey(Condicao_pelos, on_delete=models.CASCADE)
	ectoparasitas = models.ForeignKey(Ectoparasitas, on_delete=models.CASCADE)
	boca = models.ForeignKey(Boca, on_delete=models.CASCADE)
	unhas = models.ForeignKey(Unhas, on_delete=models.CASCADE)
	olhos = models.ForeignKey(Olhos, on_delete=models.CASCADE)
	patas = models.ForeignKey(Patas, on_delete=models.CASCADE)
	orelhas = models.ForeignKey(Orelhas, on_delete=models.CASCADE)
	doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)
	funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	created = models.DateField('Criado em', auto_now_add=True, auto_now=False)
	obs = models.TextField('', max_length=400, blank=True, null=True)
	

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {} - {}'.format(self.pk, self.pet.pk, self.created.strftime('%d-%m-%Y'))

	