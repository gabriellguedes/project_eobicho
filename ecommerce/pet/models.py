from django.db import models
from ecommerce.pet.tuplas import Tuplas

t = Tuplas()


class Pet(models.Model):
	
	
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


