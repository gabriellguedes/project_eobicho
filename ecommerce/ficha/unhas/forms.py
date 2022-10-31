from django import forms
from .models import *

class UnhasForm(forms.ModelForm):
	class Meta:
		model = Unhas
		fields = '__all__'