from django import forms
from .models import *

class EctoparasitasForm(forms.ModelForm):
	class Meta:
		model = Ectoparasitas
		fields = '__all__'

class PeleForm(forms.ModelForm):
	class Meta:
		model = Pele
		fields =  '__all__'

class DoencaPeleForm(forms.ModelForm):
	class Meta:
		model = DoencaPele
		fields = '__all__'