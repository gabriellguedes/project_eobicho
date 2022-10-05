from django import forms
from django.contrib.auth.models import User
from .models import Cliente, Funcionario

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['telefone'].widget.attrs.update({'class': 'mask-tel'})
		self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})	

class FuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario
		fields = '__all__'