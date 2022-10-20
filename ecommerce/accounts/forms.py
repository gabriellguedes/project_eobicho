from django import forms
from django.contrib.auth.models import User
from .models import Profile, Endereco


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	
		self.fields['telefone'].widget.attrs.update({'class': 'mask-tel'})
		self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})	

class ProfileUpdateForm(forms.ModelForm):
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
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'email')
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class EnderecoForm(forms.ModelForm):
	class Meta:
		model = Endereco
		fields = '__all__'

