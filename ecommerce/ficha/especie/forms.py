from django import forms
from .models import *

class EspecieForm(forms.ModelForm):
	class Meta:
		model = Especie
		fields = '__all__'
