from django import forms
from .models import *

class BocaForm(forms.ModelForm):
	class Meta:
		model = Boca
		fields = '__all__'