from django import forms
from localflavor.br.forms import BRCPFField
from localflavor.br.forms import BRZipCodeField
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import Profile, Endereco
from ecommerce.pet.forms import DateInput

# Dados do Usuário
class ProfileForm(forms.ModelForm):
	cpf = BRCPFField(label='CPF', required='True')
	class Meta:
		model = Profile
		fields = '__all__'
		widgets = {'aniversario': DateInput()}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	
		self.fields['telefone'].widget.attrs.update({'class': 'mask-tel'})
		self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})	

# Atualização dos dados do perfil Feita pelo cliente
class ProfileUpdateForm(forms.ModelForm):
	aniversario = forms.DateField(input_formats=['%d/%m/%Y'])
	cpf = BRCPFField(label='CPF', required='True')
	photo = forms.CharField(label='', required='False')
	class Meta:
		model = Profile
		fields = ('photo', 'cpf', 'telefone', 'aniversario')
		widgets = {'aniversario': DateInput()}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['photo'].widget.attrs.update({'class': 'd-none'})
		self.fields['telefone'].widget.attrs.update({'class': 'mask-tel'})
		self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
		self.fields['aniversario'].widget.attrs.update({'class': 'mask-date'})		

# Atualização dos dados do perfil Feita pelo gerente
class ProfileUpdateFullForm(forms.ModelForm):
	aniversario = forms.DateField(input_formats=['%d/%m/%Y'])
	cpf = BRCPFField(label='CPF', required='True')
	photo = forms.CharField(label='', required='False')
	class Meta:
		model = Profile
		fields = ('photo', 'cpf', 'telefone', 'aniversario', 'cargo')
		widgets = {'aniversario': DateInput()}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['photo'].widget.attrs.update({'class': 'd-none'})
		self.fields['telefone'].widget.attrs.update({'class': 'mask-tel'})
		self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
		self.fields['aniversario'].widget.attrs.update({'class': 'mask-date'})	


# Formulário de Login		
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Cadastro de um novo Usuário 
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
    	label='Senha',
    	strip=False,
        widget=forms.PasswordInput(),
    	)
    first_name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ('first_name', 'email')

    def clean_first_name(self):
    	nome = self.cleaned_data['first_name']
    	if nome == '' or nome == None:
    		raise ValidationError("O campo Nome deve ser preenchido!")
    	else:
    		return nome

    def clean_email(self):
    	email = self.cleaned_data['email']
    	if email =='':
    		raise ValidationError("O campo email deve ser preenchido!")
    	else:
    		return email

    def clean_password(self):
    	password = self.cleaned_data['password']
    	if password == '':
    		raise ValidationError("Insira uma senha.")
    	elif len(password) < 6:
    		raise ValidationError("Mínimo de 6 caracteres.")

    	else:
    		return password

# Editar Usuário no Sistema
class UserEditForm(forms.ModelForm):
	first_name = forms.CharField(label='Nome')
	email = forms.EmailField(label='Email')
	class Meta:
		model = User
		fields = ('first_name', 'email')

#Cadastro do Endereço dos usuários
class EnderecoForm(forms.ModelForm):
	cep = BRZipCodeField(label='CEP')
	class Meta:
		model = Endereco
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['cep'].widget.attrs.update({'class':'mask-cep', 'onblur':'IsCEP()'})

class ClienteAddForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('aniversario','cargo', 'cpf', 'telefone', 'user',)
		widgets = {'aniversario': DateInput()}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	
		self.fields['telefone'].widget.attrs.update({'class': 'mask-tel'})
		self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})	


