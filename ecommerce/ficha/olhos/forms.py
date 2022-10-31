from django import forms
from .models import *

class OlhosForm(forms.ModelForm):
	class Meta:
		model = Olhos
		fields = '__all__'