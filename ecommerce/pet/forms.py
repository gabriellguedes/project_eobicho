from django import forms
from datetime import datetime
from .models import Pet, Peso

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
		fields = '__all__'
