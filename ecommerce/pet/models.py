from django.db import models
from ecommerce.accounts.models import Cliente
from ecommerce.core.models import TimeStampedModel
from ecommerce.pet.tuplas import Tuplas

t = Tuplas()

class Especie(models.Model):
	especie = models.CharField(max_length=100, unique=True)

	class Meta:
		ordering = ('especie',)

	def __str__(self):
		return self.especie

class Raca(models.Model):
	especie = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='raças')
	raca = models.CharField(max_length=100, unique=True)

	class Meta:
		ordering = ('raca',)
	
	def __str__(self):
		return '{} - {}'.format(self.especie, self.raca)


class Pet(models.Model):
	tutor = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
	nome = models.CharField('Nome',max_length=150)
	aniversario = models.DateField('Aniversário', blank=True, null=True)
	pelagem = models.CharField('Pelagem',max_length=150, choices=t.PELAGEM_CHOICES)
	type_pelo = models.CharField('Pelo', max_length=150, blank=True, null=True, choices=t.TYPE_PELO_CHOICES)
	coloracao = models.CharField('Coloração',max_length=60, blank=True, null=True, choices=t.COLORACAO_CHOICES)
	temperamento = models.CharField('Temperamento', max_length=60, choices=t.TEMPERAMENTO_CHOICES, default=None, null=True)
	especie = models.ForeignKey(Especie, on_delete=models.SET_NULL, null=True, blank=True)
	raca = models.ForeignKey(Raca, on_delete=models.SET_NULL, null=True, blank=True)
	sexo = models.CharField('Sexo', max_length=10, choices=t.SEXO_CHOICES,default=True)
	castracao = models.BooleanField('Castrado(a)', default=False)
	status = models.BooleanField(default=True)

	class Meta:
		ordering=('nome',)

	def __str__(self):
		return '{} - {} - {}'.format(self.nome, self.id, self.status)

	def id_formated(self):
		if self.id:
			return str(self.id).zfill(4)
		return '----'

class Peso(TimeStampedModel):
	peso = models.DecimalField('Peso(kg)', max_digits=6, decimal_places=3)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
	class Meta:
		ordering = ('created',)

	def __str__(self):
		return '{} - {}'.format(self.peso, self.created.strftime('%d-%m-%Y'))

