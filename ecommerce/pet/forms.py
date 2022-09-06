from django import forms
from datetime import datetime
from .models import PetModel, AnamneseModel

class formPet(forms.ModelForm):
	aniversario = forms.DateField(
        label = (u'Aniversário'),
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'maxlength':'10',}), 
        input_formats=['%d/%m/%Y',]
    )

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

