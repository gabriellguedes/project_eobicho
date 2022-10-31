from django.db import models
from ecommerce.pet.tuplas import Tuplas
from ecommerce.pet.models import Pet
from django.contrib.auth.models import User
from ecommerce.core.models import TimeStampedModel

t = Tuplas()

class Peso(TimeStampedModel):
	peso = models.DecimalField('Peso(kg)', max_digits=6, decimal_places=3)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
	obs = models.TextField('Anotações', null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return '{} - {}'.format(self.peso, self.created.strftime('%d-%m-%Y'))



class Especie(models.Model):
	especie = models.CharField('Espécie', max_length=100, unique=True)

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.especie

class Raca(models.Model):
	especie = models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name='Espécie', related_name='raças')
	raca = models.CharField('Raça',max_length=100, unique=True)

	class Meta:
		ordering = ('pk',)
	
	def __str__(self):
		return '{} - {}'.format(self.especie, self.raca)

class Caracteristicas_Raca(models.Model):
	raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
	porte = models.CharField('Porte', max_length=15, choices=t.PORTE_RACAS_CHOICES)
	altura = models.PositiveIntegerField('Altura (cm)',)
	comprimento = models.PositiveIntegerField('Comprimento (cm)',)

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.pk 

class Doenca(models.Model):
	doenca = models.CharField(max_length=150)
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return  self.doenca

class Pele(models.Model):
	tipo_pele = models.CharField('Outros', max_length=100)
	
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
	peleInfeccionada = models.CharField('Infecção na Pele', max_length=100)
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.peleInfeccionada		

class Pelos(models.Model):
	pelos = models.CharField('Pelos', max_length=100)

	class Meta:
		ordering =('pk',)

	def __str__(self):
		return self.pelos

class Estado_pelos(models.Model):	
	pelosEstado = models.CharField('Estado do Pelo', max_length=100)
	class Meta:
		ordering =('pk',)

	def __str__(self):
		return self.pelosEstado

class Condicao_pelos(models.Model):
	pelosCondicao = models.CharField('Condição dos Pelos', max_length=100)
	class Meta:
		ordering =('pk',)

	def __str__(self):
		return self.pelosCondicao

class Boca(models.Model):
	boca = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return self.boca	

class Unhas(models.Model):
	unhas = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return self.unhas

class Olhos(models.Model):
	olhos = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return self.olhos
class Patas(models.Model):
	patas = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return self.patas

class Orelhas(models.Model):
	orelhas = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	
	def __str__(self):
		return self.orelhas

class Ficha(models.Model):
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='fichaPets')
	pele = models.ForeignKey(Pele, on_delete=models.CASCADE, verbose_name='Tipo de Pele')
	peleInfeccionada = models.ForeignKey(Infec_pele, on_delete=models.CASCADE, verbose_name='Doença na Pele')
	pelos = models.ForeignKey(Pelos, on_delete=models.CASCADE, verbose_name='Pelos')
	pelosEstado = models.ForeignKey(Estado_pelos, on_delete=models.CASCADE, verbose_name='Estado dos Pelos')
	pelosCondicao = models.ForeignKey(Condicao_pelos, on_delete=models.CASCADE, verbose_name='Condição dos Pelos')
	ectoparasitas = models.ForeignKey(Ectoparasitas, on_delete=models.CASCADE, verbose_name='Ectoparasitas')
	boca = models.ForeignKey(Boca, on_delete=models.CASCADE, verbose_name='Boca')
	unhas = models.ForeignKey(Unhas, on_delete=models.CASCADE, verbose_name='Unhas')
	olhos = models.ForeignKey(Olhos, on_delete=models.CASCADE, verbose_name='Olhos')
	patas = models.ForeignKey(Patas, on_delete=models.CASCADE, verbose_name='Patas')
	orelhas = models.ForeignKey(Orelhas, on_delete=models.CASCADE, verbose_name='Orelhas')
	doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE, verbose_name='Doença')
	funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateField('Criado em', auto_now_add=True, auto_now=False, null=True)
	obs = models.TextField('', max_length=400, blank=True, null=True)
	

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {} - {}'.format(self.pk, self.pet.pk, self.created.strftime('%d-%m-%Y'))

	