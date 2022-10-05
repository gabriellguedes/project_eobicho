from django import forms
from .models import Ficha, Pele, Pelos, Doenca, Ectoparasitas, Infec_pele, Estado_pelos, Condicao_pelos, Boca, Unhas, Olhos, Orelhas, Patas

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
