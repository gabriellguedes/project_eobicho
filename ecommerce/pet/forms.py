from django import forms
from datetime import datetime
from .models import Pet

class DateInput(forms.DateInput):
	input_type = 'date'

class PetForm(forms.ModelForm):
	class Meta:
		model = Pet
		fields = '__all__'
		widgets = {'aniversario': DateInput()}

class PetClienteAddForm(forms.ModelForm):
	class Meta:
		model = Pet
		fields = ('photo', 'nome', 'aniversario', 
				'especie', 'raca', 'temperamento', 
				'coloracao', 'type_pelo', 'pelagem', 'sexo', 'castracao',
				)
		widgets = {'aniversario': DateInput()}
		
