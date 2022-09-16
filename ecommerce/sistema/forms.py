from django import forms
from .models import Raca, Especie

class EspecieForm(forms.ModelForm):
	class Meta:
		model = Especie
		fields = '__all__'

class RacaForm(forms.ModelForm):
	class Meta:
		model = Raca
		fields = '__all__'
