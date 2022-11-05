from django.db import models

class Pelos(models.Model):
	nome = models.CharField('Pelos', max_length=100)

	class Meta:
		ordering =('pk',)

	def __str__(self):
		return self.nome

class Pelagem(models.Model):
	nome = models.CharField('Pelagem', max_length=50)
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.nome

class Coloracao(models.Model):
	nome = models.CharField('Coloração', max_length=50)
	class Meta:
		ordering = ('pk',)
	
	def __str__(self):
		return self.nome
		
class Estado_pelos(models.Model):	
	nome = models.CharField('Estado do Pelo', max_length=100)
	class Meta:
		ordering =('pk',)

	def __str__(self):
		return self.nome

class Condicao_pelos(models.Model):
	nome = models.CharField('Condição dos Pelos', max_length=100)
	class Meta:
		ordering =('pk',)

	def __str__(self):
		return self.nome
