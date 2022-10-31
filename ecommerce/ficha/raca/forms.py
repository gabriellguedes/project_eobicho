from django import forms
from .models import *

class RacaForm(forms.ModelForm):
	class Meta:
		model = Raca
		fields = '__all__'

class Caracteristicas_RacaForm(forms.ModelForm):
	class Meta:
		model= Caracteristicas_Raca
		fields = '__all__'
