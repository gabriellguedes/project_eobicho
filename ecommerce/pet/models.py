from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ecommerce.core.models import TimeStampedModel
from ecommerce.pet.tuplas import Tuplas

import uuid
import os 


t = Tuplas()

def upload_image_formater(instance, filename):
	return f'{str(uuid.uuid4())}-{filename}'



class Pet(models.Model):
	photo = models.ImageField('Foto do Pet', upload_to=upload_image_formater, blank=True, null=True)
	tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	nome = models.CharField('Nome',max_length=150)
	aniversario = models.DateField('Aniversário', blank=True, null=True)
	pelagem = models.CharField('Pelagem',max_length=150, choices=t.PELAGEM_CHOICES)
	type_pelo = models.CharField('Pelo', max_length=150, blank=True, null=True, choices=t.TYPE_PELO_CHOICES)
	coloracao = models.CharField('Coloração',max_length=60, blank=True, null=True, choices=t.COLORACAO_CHOICES)
	temperamento = models.CharField('Temperamento', max_length=60, choices=t.TEMPERAMENTO_CHOICES, default=None, null=True)
	sexo = models.CharField('Sexo', max_length=10, choices=t.SEXO_CHOICES,default=True)
	castracao = models.BooleanField('Castrado(a)', default=False)
	status = models.BooleanField(default=True)

	def has_image(self):
		return self.photo != None and self.image != ''

	def remove_image(self):
		if self.has_image():
			if os.path.isfile(self.photo.path):
				os.remove(self.photo.path)
		self.photo = None

	def delete(self):
		self.remove_image()
		super().delete()
				
	class Meta:
		ordering=('nome',)

	def get_absolute_url(self):
		return reverse_lazy('pet:pet_detail', kwargs={'pk': self.pk})
	
	def __str__(self):
		return '{} - {} - {}'.format(self.nome, self.id, self.status)




