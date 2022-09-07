from django.contrib.auth.models import User
from django.db import models
from ecommerce.core.models import TimeStampedModel
from ecommerce.pet.tuplas import Tuplas

t = Tuplas()


class PetModel(models.Model):
	nome = models.CharField('Nome',max_length=150)
	apelido = models.CharField('Apelido',max_length=30)
	aniversario = models.DateField('Aniversário', blank=True, null=True)
	idade = models.PositiveIntegerField('Idade', blank=True, null=True)
	peso = models.DecimalField('Peso(kg)', max_digits=7, decimal_places=3, blank=True, null=True)
	tamanho = models.PositiveIntegerField('Tamanho(cm)')
	especie = models.CharField('Especie',max_length=10, choices=t.ESPECIE_CHOICES)
	racaCachorro = models.CharField('Raça do Cachorro',max_length=150, blank=True, null=True, choices=t.RACA_CACHORRO)
	racaGato = models.CharField('Raça do Gato', max_length=250, blank=True, null=True, choices=t.RACA_GATO)
	temperamento = models.CharField('Temperamento',max_length=60, choices=t.TEMPERAMENTO_CHOICES)
	pelagem = models.CharField('Pelagem',max_length=150, choices=t.PELAGEM_CHOICES)
	type_pelo = models.CharField('Pelo', max_length=150, blank=True, null=True, choices=t.TYPE_PELO_CHOICES)
	coloracao = models.CharField('Coloração',max_length=60, blank=True, null=True, choices=t.COLORACAO_CHOICES)
	caracteristicas = models.CharField('Caracteristicas', max_length=200)
	
	def __str__(self):
		return self.nome	

class AnamneseModel(models.Model):
	funcionario = models.ForeignKey(User, models.SET_NULL, null=True)
	pet = models.ForeignKey(PetModel, on_delete=models.CASCADE, related_name='fichaPets')
	unhas = models.CharField('', max_length=100, blank=True, null=True, choices=t.UNHAS_CHOICES)
	ectoparasitas = models.CharField('Ectoparasitas', blank=True, null=True, max_length=100, choices=t.ECTOPARASITAS_CHOICES)
	peleInfeccionada = models.CharField('Infecção na Pele', max_length=100, blank=True, null=True, choices=t.PELE_INFECCIONADA_CHOICES)
	peleOutros = models.CharField('Outros', max_length=100, blank=True, null=True, choices=t.PELE_OUTROS_CHOICES)
	pelos = models.CharField('Pelos', max_length=100, blank=True, null=True, choices=t.PELOS_CHOICES)
	pelosEstado = models.CharField('Estado do Pelo', max_length=100, blank=True, null=True, choices=t.PELOS_ESTADO_CHOICES)
	pelosCondicao = models.CharField('Condição dos Pelos', max_length=100, blank=True, null=True, choices=t.PELOS_CONDICAO_CHOICES)
	boca = models.CharField('', max_length=100, blank=True, null=True, choices=t.BOCA_CHOICES)
	olhos = models.CharField('', max_length=100, blank=True, null=True, choices=t.OLHOS_CHOICES)
	patas = models.CharField('', max_length=100, blank=True, null=True, choices=t.PATAS_CHOICES)
	orelhas = models.CharField('', max_length=100, blank=True, null=True, choices=t.ORELHAS_CHOICES)
	doenca = models.CharField('', max_length=100, choices=t.DOENCA_CHOICES)
	obs = models.TextField('', max_length=400, blank=True, null=True)

	class Meta:
		ordering = ('pk',)
	def __str__(self):
		return '{} - {}'.format(self.pk, self.pet.pk)
