from django import forms
from .models import Ficha, Prontuario, Pele, Pelos, Doenca

class ProntuarioForm(forms.ModelForm):
	model = Prontuario
	fields = '__all__'

class DoencaForm(forms.ModelForm):
	class Meta:
		model = Doenca
		fields = '__all__'

class PeleForm(forms.ModelForm):
	class Meta:
		model = Pele
		fields =  '__all__'

class PelosForm(forms.ModelForm):
	class Meta:
		model = Pelos
		fields = '__all__'

class FichaForm(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = '__all__'