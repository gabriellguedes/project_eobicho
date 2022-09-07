from django import forms
from datetime import datetime
from .models import PetModel, AnamneseModel

class formPet(forms.ModelForm):
	class Meta:
		model = PetModel
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['aniversario'].widget.attrs.update({'class': 'date'})
		
class anamneseForm(forms.ModelForm):
	class Meta:
		model = AnamneseModel
		fields = '__all__'

