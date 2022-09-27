from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def login(request):
	template_name = 'index.html'
	
	return render(request,template_name)


