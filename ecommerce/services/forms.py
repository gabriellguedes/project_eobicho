from django import forms
from .models import Ficha, Banho, Tosa, Itens

class BanhoForm(forms.ModelForm):
	class Meta:
		 model = Banho
		 fields ='__all__'

class TosaForm(forms.ModelForm):
	class Meta:
		model = Tosa
		fields = '__all__'

class ItensForm(forms.ModelForm):
	class Meta:
		model = Itens
		fields = '__all__'

class FichaForm(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = '__all__'
