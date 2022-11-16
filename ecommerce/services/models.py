from django.db import models
from ecommerce.pet.models import Pet
from django.contrib.auth.models import User
from ecommerce.core.models import TimeStampedModel

# Create your models here.
STATUS_CHOICES = [
	('aguardando', 'aguardando'),
	('aprovado','aprovado'),
	('atendendo','atendendo'),
	('alterado','alterado'),
	('cancelado', 'cancelado'),
]
class Itens(models.Model):
	nome= models.CharField('Itens', max_length=100)

	def __str__(self):
		return self.nome

class Banho(models.Model):
	nome = models.CharField('Banho', max_length=100)

	def __str__(self):
		return self.nome

class Tosa(models.Model):
	nome = models.CharField('Tosa', max_length=100)

	def __str__(self):
		return self.nome

class Ficha(TimeStampedModel):
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='FichaBanho')
	funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='')
	status = models.CharField('', max_length=20 ,choices=STATUS_CHOICES, blank=True, default='aguardando')
	banho = models.ManyToManyField(Banho, verbose_name='Banho')
	tosa = models.ManyToManyField(Tosa, verbose_name='Tosa' )
	itens = models.ManyToManyField(Itens, verbose_name='Itens do Pet')
	outros = models.CharField('Outros Itens', max_length=100, blank=True, null=True)
	
	class Meta:
		ordering =('created',)
		
	def __str__(self):
		return '{} - {}'.format(self.pk, self.created.strftime('%d/%m/%Y'))