from django import forms
from localflavor.br.forms import BRCPFField
from localflavor.br.forms import BRZipCodeField
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import Profile, Endereco


class ProfileForm(forms.ModelForm):
	cpf = BRCPFField(label='CPF', required='True')
	class Meta:
		model = Profile
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	
		self.fields['telefone'].widget.attrs.update({'class': 'mask-tel'})
		self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})	

class ProfileUpdateForm(forms.ModelForm):
	cpf = BRCPFField(label='CPF', required='True')
	class Meta:
		model = Profile
		fields = ('photo','telefone', 'cpf')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['telefone'].widget.attrs.update({'class': 'mask-tel'})
		self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})	
		
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
    	label='Senha',
    	strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    	)

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
    	else:
    		return password
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class EnderecoForm(forms.ModelForm):
	cep = BRZipCodeField(label='CEP')
	class Meta:
		model = Endereco
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['cep'].widget.attrs.update({'class':'mask-cep', 'onblur':'IsCEP()'})


