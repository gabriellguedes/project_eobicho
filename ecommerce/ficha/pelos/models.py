from django.db import models

class Pelos(models.Model):
	pelos = models.CharField('Pelos', max_length=100)

	class Meta:
		ordering =('pk',)

	def __str__(self):
		return self.pelos

class Pelagem(models.Model):
	pelagem = models.CharField('Pelagem', max_length=50)
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.pelagem

class Coloracao(models.Model):
	coloracao = models.CharField('Coloração', max_length=50)
	class Meta:
		ordering = ('pk',)
	
	def __str__(self):
		return self.coloracao
		
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
