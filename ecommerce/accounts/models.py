from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ecommerce.pet.models import Tuplas
import uuid

t = Tuplas()

def upload_image_formater(instance, filename):
	return f'{str(uuid.uuid4())}-{filename}'

class Profile(models.Model):
	status = models.BooleanField(default=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	cargo = models.CharField('', max_length=50,choices=t.CARGOS_CHOICES, default='Cliente')
	photo = models.ImageField('Foto de Perfil',  upload_to=upload_image_formater, blank=True, null=True)
	cpf = models.CharField('CPF', max_length=15, unique=True)
	telefone = models.CharField('Telefone', max_length=16, null=True, blank=True)

	class Meta:
		ordering = ('pk',)

	def get_absolute_url(self):
		return reverse_lazy('contas:cliente_detail', kwargs={'pk': self.pk})
	
		
	def __str__(self):
		return '{} - {}'.format(self.pk, self.user.first_name) 

class Endereco(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
	cep = models.CharField('CEP',max_length=10)
	uf = models.CharField('UF',max_length=2, choices=t.UF_CHOICES)
	cidade = models.CharField('Cidade', max_length=100)
	bairro = models.CharField('Bairro', max_length=100)
	endereco = models.CharField('Endereço', max_length=200)
	complemento = models.CharField('Complemento', max_length=200)

	def __str__(self):
		return self.pk
