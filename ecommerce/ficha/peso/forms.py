from django import forms
from .models import *

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

