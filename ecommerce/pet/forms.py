from django import forms
from datetime import datetime
from .models import Pet, Peso, Raca, Especie

class EspecieForm(forms.ModelForm):
	class Meta:
		model = Especie
		fields = '__all__'

class RacaForm(forms.ModelForm):
	class Meta:
		model = Raca
		fields = '__all__'

class PetForm(forms.ModelForm):
	class Meta:
		model = Pet
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['aniversario'].widget.attrs.update({'class': 'mask-date'})
		
class PesoForm(forms.ModelForm):
	class Meta:
		model = Peso
		fields = ('peso', 'obs')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['peso'].widget.attrs.update({'class': 'mask-peso'})

class PesoUpdateForm(forms.ModelForm):
	class Meta:
		model = Peso
		fields = ('peso', 'obs')