from django.db import models
from ecommerce.pet.tuplas import Tuplas
from ecommerce.pet.models import Pet
from ecommerce.ficha.boca.models import Boca
from ecommerce.ficha.doenca.models import Doenca
from ecommerce.ficha.especie.models import Especie
from ecommerce.ficha.olhos.models import Olhos
from ecommerce.ficha.orelhas.models import Orelhas
from ecommerce.ficha.patas.models import Patas
from ecommerce.ficha.pele.models import Pele, Ectoparasitas, Infec_pele
from ecommerce.ficha.pelos.models import Pelos, Estado_pelos, Condicao_pelos
from ecommerce.ficha.unhas.models import Unhas
from django.contrib.auth.models import User
from ecommerce.core.models import TimeStampedModel

t = Tuplas()

class Ficha(models.Model):
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='fichaPets')
	pele = models.ManyToManyField(Pele, verbose_name='Tipo de Pele')
	peleInfeccionada = models.ManyToManyField(Infec_pele, verbose_name='Doença na Pele')
	pelos = models.ManyToManyField(Pelos, verbose_name='Pelos')
	pelosEstado = models.ManyToManyField(Estado_pelos, verbose_name='Estado dos Pelos')
	pelosCondicao = models.ManyToManyField(Condicao_pelos, verbose_name='Condição dos Pelos')
	ectoparasitas = models.ManyToManyField(Ectoparasitas, verbose_name='Ectoparasitas')
	boca = models.ManyToManyField(Boca, verbose_name='Boca')
	unhas = models.ManyToManyField(Unhas, verbose_name='Unhas')
	olhos = models.ManyToManyField(Olhos, verbose_name='Olhos')
	patas = models.ManyToManyField(Patas, verbose_name='Patas')
	orelhas = models.ManyToManyField(Orelhas, verbose_name='Orelhas')
	doenca = models.ManyToManyField(Doenca, related_name='doencas_geral')
	funcionario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Criado por', blank=True, null=True)
	created = models.DateField('Criado em', auto_now_add=True, auto_now=False, null=True)
	obs = models.TextField('', max_length=400, blank=True, null=True)
	

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {} - {}'.format(self.pk, self.pet.pk, self.created.strftime('%d-%m-%Y'))

	