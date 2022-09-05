from django import forms
from datetime import datetime
from .models import PetModel

class formPet(forms.ModelForm):
	aniversario = forms.DateField(
        label = (u'Aniversário'),
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'maxlength':'10',}), 
        input_formats=['%d/%m/%Y',]
    )
	class Meta:
		model = PetModel
		fields = '__all__'
