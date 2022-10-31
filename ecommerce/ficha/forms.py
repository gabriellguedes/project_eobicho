from django import forms
from .models import *

class FichaForm(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = '__all__'
