from django.db import models
from ecommerce.pet.tuplas import Tuplas
from ecommerce.pet.models import Pet
from django.contrib.auth.models import User

t = Tuplas()

class Ficha(models.Model):
	
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='fichaPets')
	unhas = models.CharField('', max_length=100, choices=t.UNHAS_CHOICES)
	ectoparasitas = models.CharField('Ectoparasitas',  max_length=100, choices=t.ECTOPARASITAS_CHOICES)
	peleInfeccionada = models.CharField('Infecção na Pele', max_length=100,  choices=t.PELE_INFECCIONADA_CHOICES)
	peleOutros = models.CharField('Outros', max_length=100, choices=t.PELE_OUTROS_CHOICES)
	pelos = models.CharField('Pelos', max_length=100, choices=t.PELOS_CHOICES)
	pelosEstado = models.CharField('Estado do Pelo', max_length=100, choices=t.PELOS_ESTADO_CHOICES)
	pelosCondicao = models.CharField('Condição dos Pelos', max_length=100, choices=t.PELOS_CONDICAO_CHOICES)
	boca = models.CharField('', max_length=100, choices=t.BOCA_CHOICES)
	olhos = models.CharField('', max_length=100, choices=t.OLHOS_CHOICES)
	patas = models.CharField('', max_length=100, choices=t.PATAS_CHOICES)
	orelhas = models.CharField('', max_length=100, choices=t.ORELHAS_CHOICES)
	doenca = models.CharField('', max_length=100, choices=t.DOENCA_CHOICES)
	obs = models.TextField('', max_length=400, blank=True, null=True)
	date = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return '{} - {}'.format(self.pk, self.pet.pk)