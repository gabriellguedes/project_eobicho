from django import forms
from .models import *

class DoencaForm(forms.ModelForm):
	class Meta:
		model = Doenca
		fields = '__all__'