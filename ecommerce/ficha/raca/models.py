from django.db import models
from ecommerce.pet.tuplas import Tuplas
from ecommerce.ficha.especie.models import Especie

t = Tuplas()

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
		return str(self.pk) 