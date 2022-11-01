from django import forms
from .models import Temperamento

class TemperamentoForm(forms.ModelForm):
	class Meta:
		model = Temperamento
		fields = '__all__'