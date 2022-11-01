from django.db import models

class Temperamento(models.Model):
	temperamento = models.CharField('Temperamento', max_length=50)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return self.temperamento