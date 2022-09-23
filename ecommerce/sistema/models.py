from django.db import models

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
