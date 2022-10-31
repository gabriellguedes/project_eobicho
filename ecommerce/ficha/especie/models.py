from django.db import models

class Especie(models.Model):
	especie = models.CharField('Espécie', max_length=100, unique=True)

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return self.especie
