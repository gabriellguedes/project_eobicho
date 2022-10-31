from django.db import models
from ecommerce.pet.models import Pet
from django.contrib.auth.models import User
from ecommerce.core.models import TimeStampedModel

class Peso(TimeStampedModel):
	peso = models.DecimalField('Peso(kg)', max_digits=6, decimal_places=3)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
	obs = models.TextField('Anotações', null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return '{} - {}'.format(self.peso, self.created.strftime('%d-%m-%Y'))