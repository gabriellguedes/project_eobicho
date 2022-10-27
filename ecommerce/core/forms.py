from django import forms
from .models import TimeStampedModel

class TimeStampedForm(forms.ModelForm):
	class Meta:
		model = TimeStampedModel
		fields = '__all__'