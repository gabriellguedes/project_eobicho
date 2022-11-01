from django import forms
from .models import *

class PelosForm(forms.ModelForm):
	class Meta:
		model = Pelos
		fields = '__all__'

class PelagemForm(forms.ModelForm):
	class Meta:
		model = Pelagem
		fields = '__all__'

class ColoracaoForm(forms.ModelForm):
	class Meta:
		model = Coloracao
		fields = '__all__'

class Estado_pelosForm(forms.ModelForm):
	class Meta:
		model = Estado_pelos
		fields = '__all__'

class Condicao_pelosForm(forms.ModelForm):
	class Meta:
		model = Condicao_pelos
		fields = '__all__'