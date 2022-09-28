from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
	nome = models.CharField('Nome', max_length=150)
	cpf = models.CharField('CPF', max_length=15, unique=True)
	email = models.EmailField('Email')
	telefone = models.CharField('Telefone', max_length=16)

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.nome) 

	def id_formated(self):
		if self.pk:
			return str(self.pk).zfill(3)
		return '---'

class Funcionario(models.Model):
	status = models.BooleanField(default=True)
	nome = models.CharField('Nome', max_length=150)
	email = models.EmailField('Email')
	telefone = models.CharField('Telefone', max_length=16)
	
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{}-{}'.format(self.pk, self.nome) 

	def id_formated(self):
		if self.pk:
			return str(self.pk).zfill(3)
		return '---'		
