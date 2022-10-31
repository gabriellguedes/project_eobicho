from django import forms
from .models import *


class OrelhasForm(forms.ModelForm):
	class Meta:
		model = Orelhas
		fields = '__all__'
