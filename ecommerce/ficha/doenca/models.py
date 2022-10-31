from django.db import models

class Doenca(models.Model):
	doenca = models.CharField(max_length=150)
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return  self.doenca
