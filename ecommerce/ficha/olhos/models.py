from django.db import models


class Olhos(models.Model):
	olhos = models.CharField('', max_length=100)
	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return self.olhos