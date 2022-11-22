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
		fields = ('nome', 'aniversario', 
				'especie', 'raca', 'temperamento', 
				'coloracao', 'type_pelo', 'pelagem', 'sexo', 'castracao',
				)
		widgets = {'aniversario': DateInput()}

class PetUpdateForm(forms.ModelForm):
	aniversario = forms.DateField(input_formats=['%d/%m/%Y'])
	class Meta:
		model = Pet
		fields = '__all__'
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['aniversario'].widget.attrs.update({'class':'mask-date'})

class PetClienteUpdateForm(forms.ModelForm):
	aniversario = forms.DateField(input_formats=['%d/%m/%Y'])
	class Meta:
		model = Pet
		fields = ('photo', 'nome', 'aniversario', 
				'especie', 'raca', 'temperamento', 
				'coloracao', 'type_pelo', 'pelagem', 'sexo', 'castracao',
				)
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['aniversario'].widget.attrs.update({'class':'mask-date'})
		
