from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ecommerce.pet.models import Tuplas
import uuid

t = Tuplas()

def upload_image_formater(instance, filename):
	return f'{str(uuid.uuid4())}-{filename}'

class Cliente(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	photo = models.ImageField('Foto de Perfil',  upload_to=upload_image_formater, blank=True, null=True)
	cpf = models.CharField('CPF', max_length=15, unique=True)
	telefone = models.CharField('Telefone', max_length=16, null=True, blank=True)

	class Meta:
		ordering = ('pk',)

	def get_absolute_url(self):
		return reverse_lazy('contas:cliente_detail', kwargs={'pk': self.pk})
	
		
	def __str__(self):
		return '{} - {}'.format(self.pk, self.user.first_name) 

	def id_formated(self):
		if self.pk:
			return str(self.pk).zfill(3)
		return '---'

class Funcionario(models.Model):
	status = models.BooleanField(default=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	cargo = models.CharField('Cargo', max_length=50,choices=t.CARGOS_CHOICES)
	telefone = models.CharField('Telefone', max_length=16)
	
	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{}-{}'.format(self.pk, self.nome) 

	def id_formated(self):
		if self.pk:
			return str(self.pk).zfill(3)
		return '---'		
