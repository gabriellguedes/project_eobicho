from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from ecommerce.accounts.models import Cliente
from ecommerce.accounts.forms import ClienteForm


def login(request):
	if request.user.is_authenticated:
		user = request.user
		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': user.id }))
	else:
		return HttpResponseRedirect(reverse('contas:login'))

def photo_user(request):
	template_name = 'includes/user_block.html'
	user = request.user
	obj = Cliente.objects.get(user=user)
	context = {'user_obj': obj}
	return render(request, template_name, context=context)
