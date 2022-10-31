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

class Infec_peleForm(forms.ModelForm):
	class Meta:
		model = Infec_pele
		fields = '__all__'