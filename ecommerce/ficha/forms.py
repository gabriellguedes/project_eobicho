from django import forms
from ecommerce.ficha.models import Ficha

class FichaForm(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = '__all__'