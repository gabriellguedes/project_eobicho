from django import forms
from datetime import datetime
from .models import formPet

class CadastroPet(forms.ModelForm):
	aniversario = forms.DateField(
        label = (u'Aniversário'),
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'maxlength':'10',}), 
        input_formats=['%d/%m/%Y',]
    )
	class Meta:
		model = formPet
		fields = '__all__'
