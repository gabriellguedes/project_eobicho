from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from ecommerce.accounts.models import Cliente
from ecommerce.accounts.forms import ClienteForm


def home(request):
	template_name='core/index.html'
	if request.user.is_authenticated:
		user = request.user
		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': user.id }))
	else:
		return HttpResponseRedirect(reverse('contas:login'))

def permission(request):
	template_name='core/permission.html'
	return render(request, template_name)