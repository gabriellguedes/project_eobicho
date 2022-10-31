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
	pele = models.ForeignKey(Pele, on_delete=models.CASCADE, verbose_name='Tipo de Pele')
	peleInfeccionada = models.ForeignKey(Infec_pele, on_delete=models.CASCADE, verbose_name='Doença na Pele')
	pelos = models.ForeignKey(Pelos, on_delete=models.CASCADE, verbose_name='Pelos')
	pelosEstado = models.ForeignKey(Estado_pelos, on_delete=models.CASCADE, verbose_name='Estado dos Pelos')
	pelosCondicao = models.ForeignKey(Condicao_pelos, on_delete=models.CASCADE, verbose_name='Condição dos Pelos')
	ectoparasitas = models.ForeignKey(Ectoparasitas, on_delete=models.CASCADE, verbose_name='Ectoparasitas')
	boca = models.ForeignKey(Boca, on_delete=models.CASCADE, verbose_name='Boca')
	unhas = models.ForeignKey(Unhas, on_delete=models.CASCADE, verbose_name='Unhas')
	olhos = models.ForeignKey(Olhos, on_delete=models.CASCADE, verbose_name='Olhos')
	patas = models.ForeignKey(Patas, on_delete=models.CASCADE, verbose_name='Patas')
	orelhas = models.ForeignKey(Orelhas, on_delete=models.CASCADE, verbose_name='Orelhas')
	doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE, verbose_name='Doença')
	funcionario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Criado por', blank=True, null=True)
	created = models.DateField('Criado em', auto_now_add=True, auto_now=False, null=True)
	obs = models.TextField('', max_length=400, blank=True, null=True)
	

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {} - {}'.format(self.pk, self.pet.pk, self.created.strftime('%d-%m-%Y'))

	