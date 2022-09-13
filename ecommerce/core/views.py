from django.shortcuts import render
from .forms import RacaForm, EspecieForm
from ecommerce.pet.models import Raca, Especie
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def login(request):
	template_name = 'index.html'
	return render(request, template_name)

#Adicionar uma nova Especie
def add_Especie(request):
	template_name = 'core/add_form.html'
	form = EspecieForm(request.POST or None)
	if request.method=='POST':
		if form.is_valid():
			form = form.save()
			return HttpResponseRedirect(reverse_lazy('core:list_especie'))
	context ={'especie': form}		
	return render(request, template_name, context)

#Listar as Especies
def list_Especie(request):
	template_name = 'core/list_especie.html'
	obj = Especie.objects.all()
	context = { 'especie': obj }
	return render(request, template_name, context=context)

#Deletar uma Especie
def delete_Especie(request, pk):
	obj = Especie.objects.get(id=pk)
	obj.delete()
	
	return render(request, reverse_lazy('core:list_especie'))

# Adicionar Raça
def add_Raca(request):
	template_name = 'core/add_raca_form.html'
	form = RacaForm(request.POST)
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy('pet:list'))
	context = {
		'raca': form,
	}
	return render(request, template_name, context)
