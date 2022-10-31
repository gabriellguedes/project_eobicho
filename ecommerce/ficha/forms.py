from django import forms
from .models import *

class Caracteristicas_RacaForm(forms.ModelForm):
	class Meta:
		model= Caracteristicas_Raca
		fields = '__all__'

class PesoForm(forms.ModelForm):
	class Meta:
		model = Peso
		fields = ('peso', 'obs')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['peso'].widget.attrs.update({'class': 'mask-peso'})

class PesoUpdateForm(forms.ModelForm):
	class Meta:
		model = Peso
		fields = ('peso', 'obs')

class EspecieForm(forms.ModelForm):
	class Meta:
		model = Especie
		fields = '__all__'

class RacaForm(forms.ModelForm):
	class Meta:
		model = Raca
		fields = '__all__'

class DoencaForm(forms.ModelForm):
	class Meta:
		model = Doenca
		fields = '__all__'

class EctoparasitasForm(forms.ModelForm):
	class Meta:
		model = Ectoparasitas
		fields = '__all__'

class PeleForm(forms.ModelForm):
	class Meta:
		model = Pele
		fields =  '__all__'

class Infec_peleForm(forms.ModelForm):
	class Meta:
		model = Infec_pele
		fields = '__all__'

class PelosForm(forms.ModelForm):
	class Meta:
		model = Pelos
		fields = '__all__'

class Estado_pelosForm(forms.ModelForm):
	class Meta:
		model = Estado_pelos
		fields = '__all__'

class Condicao_pelosForm(forms.ModelForm):
	class Meta:
		model = Condicao_pelos
		fields = '__all__'

class BocaForm(forms.ModelForm):
	class Meta:
		model = Boca
		fields = '__all__'

class UnhasForm(forms.ModelForm):
	class Meta:
		model = Unhas
		fields = '__all__'

class OlhosForm(forms.ModelForm):
	class Meta:
		model = Olhos
		fields = '__all__'

class PatasForm(forms.ModelForm):
	class Meta:
		model = Patas
		fields = '__all__'

class OrelhasForm(forms.ModelForm):
	class Meta:
		model = Orelhas
		fields = '__all__'


class FichaForm(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = '__all__'
