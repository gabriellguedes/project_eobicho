from django import forms
from ecommerce.ficha.doenca.models import Doenca
from ecommerce.pet.tuplas import Tuplas
from .models import *

t = Tuplas()

class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
	input_type = 'checkbox'

class AnamneseForm(forms.ModelForm):
	class Meta:
		model = Anamnese
		fields = '__all__'

class TestForm(forms.ModelForm):
	class Meta:
		model = Anamnese
		fields = ('doenca',)
		widgets = {'doenca': CheckboxSelectMultiple()}
