from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
	created = models.DateTimeField('criado em', auto_now_add=False, auto_now=True)
	modified = models.DateTimeField('modificado em', auto_now_add=False, auto_now=True)
	
	class Meta:
		abstract = True