from django.db import models
from ecommerce.pet.models import Pet
from ecommerce.ficha.models import Anamnese
from django.contrib.auth.models import User
from ecommerce.core.models import TimeStampedModel

# Create your models here.
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
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
	funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
	banho = models.ForeignKey(Banho, on_delete=models.CASCADE)
	tosa = models.ForeignKey(Tosa, on_delete=models.CASCADE)
	itens = models.ForeignKey(Itens, on_delete=models.CASCADE)
	outros = models.CharField('Outros', max_length=100)
	anamnese = models.ForeignKey(Anamnese, on_delete=models.CASCADE)
	
	class Meta:
		ordering =('created',)
		
	def __str__(self):
		return self.pk