from django.shortcuts import render


def home(request):
	template = 'accounts/home.html'
	return template
