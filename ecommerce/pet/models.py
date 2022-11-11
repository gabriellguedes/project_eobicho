from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ecommerce.core.models import TimeStampedModel
from ecommerce.ficha.raca.models import Raca
from ecommerce.ficha.especie.models import Especie
from ecommerce.ficha.pelos.models import Pelos, Pelagem, Coloracao
from ecommerce.ficha.temperamento.models import Temperamento
from ecommerce.pet.tuplas import Tuplas

import uuid
import os 


t = Tuplas()

def upload_image_formater(instance, filename):
	return f'{str(uuid.uuid4())}-{filename}'

class Pet(models.Model):
	photo = models.ImageField('Foto do Pet', upload_to=upload_image_formater, blank=True, null=True)
	tutor = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tutores')
	nome = models.CharField('Nome',max_length=150)
	aniversario = models.DateField('Aniversário', blank=True, null=True)
	idade = models.PositiveIntegerField('Idade')
	especie = models.ForeignKey(Especie, on_delete=models.PROTECT, verbose_name='Espécie')
	raca = models.ForeignKey(Raca, on_delete=models.PROTECT, verbose_name='Raça')
	temperamento = models.ForeignKey(Temperamento, on_delete=models.PROTECT, verbose_name='Temperamento')
	coloracao = models.ForeignKey(Coloracao, on_delete=models.PROTECT, verbose_name='Cor dos Pelos')
	type_pelo = models.ForeignKey(Pelos, on_delete=models.PROTECT, verbose_name='Pelos')
	pelagem = models.ForeignKey(Pelagem, on_delete=models.PROTECT, verbose_name='Pelagem')
	sexo = models.CharField('Sexo', max_length=10, choices=t.SEXO_CHOICES,default=True)
	castracao = models.BooleanField('Castrado(a)', default=False)
	status = models.BooleanField(default=True)

	def has_image(self):
		return self.photo != None and self.image != ''

					
	class Meta:
		ordering=('nome',)

	def get_absolute_url(self):
		return reverse_lazy('pet:pet_detail', kwargs={'pk': self.pk})
	
	def __str__(self):
		return '{} - {} - {}'.format(self.nome, self.id, self.status)




