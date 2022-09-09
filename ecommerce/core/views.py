from django.shortcuts import render

def login(request):
	template_name = 'index.html'
	return render(request, template_name)
