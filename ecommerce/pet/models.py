from django.db import models
from ecommerce.pet.tuplas import Tuplas

t = Tuplas()


class PetModel(models.Model):
	nome = models.CharField('Nome',max_length=150)
	apelido = models.CharField('Apelido',max_length=30)
	aniversario = models.DateField('Aniversário', blank=True, null=True)
	idade = models.PositiveIntegerField('Idade')
	peso = models.DecimalField('Peso(kg)', max_digits=7, decimal_places=2)
	tamanho = models.PositiveIntegerField('Tamanho(cm)')
	especie = models.CharField('Especie',max_length=10, choices=t.ESPECIE_CHOICES)
	racaCachorro = models.CharField('Raça do Cachorro',max_length=150, choices=t.RACA_CACHORRO)
	temperamento = models.CharField('Temperamento',max_length=60, choices=t.TEMPERAMENTO_CHOICES)
	pelagem = models.CharField('Pelagem',max_length=150, choices=t.PELAGEM_CHOICES)
	coloracao = models.CharField('Coloração',max_length=60, choices=t.COLORACAO_CHOICES)
	caracteristicas = models.CharField('Caracteristicas', max_length=200)
	
	def __str__(self):
		return self.nome	

class AnamneseModel(models.Model):
	unhas = models.CharField('Unhas', max_length=100, choices=t.UNHAS_CHOICES)
	ectoparasitas = models.CharField('Ectoparasitas', max_length=100, choices=t.ECTOPARASITAS_CHOICES)
	peleInfeccionada = models.CharField('Infecção na Pele', max_length=100, choices=t.PELE_INFECCIONADA_CHOICES)
	peleOutros = models.CharField('Outros', max_length=100, choices=t.PELE_OUTROS_CHOICES)
	pelos = models.CharField('Pelos', max_length=100, choices=t.PELOS_CHOICES)
	pelosEstado = models.CharField('Estado do Pelo', max_length=100, choices=t.PELOS_ESTADO_CHOICES)
	pelosCondicao = models.CharField('Condição dos Pelos', max_length=100, choices=t.PELOS_CONDICAO_CHOICES)
	boca = models.CharField('Boca', max_length=100, choices=t.BOCA_CHOICES)
	olhos = models.CharField('Olhos', max_length=100, choices=t.OLHOS_CHOICES)
	patas = models.CharField('Patas', max_length=100, choices=t.PATAS_CHOICES)
	orelhas = models.CharField('Orelhas', max_length=100, choices=t.ORELHAS_CHOICES)
