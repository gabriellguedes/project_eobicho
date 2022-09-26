from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def login(request):
	template_name = 'index.html'
	data = {}
	if(request.POST['password'] != request.POST['password-conf']):
		data['msg'] = 'Senha e confirmação de senha diferentes!'
		data['class'] = 'alert-danger'
	else:
		user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
		user.first_name = request.POST['name']
		user.save()
		data['msg'] = 'Usuário cadastrado com sucesso!'
		data['class'] = 'alert-success'
	return render(request,template_name,data)


