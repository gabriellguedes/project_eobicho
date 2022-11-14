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
	banho_choices =[]
	itens_choices=[]
	tosa_choices =[]
	i= Itens.objects.all()
	t = Tosa.objects.all()
	b = Banho.objects.all()
	for x in i:
		tupla = (x.nome, x.nome)
		itens_choices.append(tupla)
	for i in t:
		tupla = (i.nome, i.nome)
		tosa_choices.append(tupla)
	for i in b:
		tupla = (i.nome, i.nome)
		banho_choices.append(tupla)
	banho = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=banho_choices,)
	itens = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=itens_choices,)
	tosa = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=tosa_choices,)
	class Meta:
		model = Ficha
		fields = '__all__'
