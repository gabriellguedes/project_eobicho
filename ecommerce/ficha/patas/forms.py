from django import forms
from .models import *


class PatasForm(forms.ModelForm):
	class Meta:
		model = Patas
		fields = '__all__'
