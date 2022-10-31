from django.db import models


class Boca(models.Model):
	boca = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return self.boca	
