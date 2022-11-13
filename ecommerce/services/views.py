from datetime import datetime
from django.shortcuts import render
from django.forms import inlineformset_factory
from django.urls import reverse
from django.http import HttpResponseRedirect
from ecommerce.pet.models import Pet
from ecommerce.pet.views import birthday
from .models import Ficha, Banho, Tosa, Itens
from .forms import FichaForm, BanhoForm, TosaForm, ItensForm

# Adicionar um tipo de banho
def banho_add(request):
	template_name = 'banho/banho_add.html'
	if request.method == 'GET':
		form = BanhoForm()
		return render(request, template_name, {'form':form})
	elif request.method == 'POST':
		form = BanhoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:banho_list'))
		else:
			return render(request, template_name, {'form':form})
# Atualizar um tipo de banho
def banho_update(request, pk):
	template_name ='banho/banho_update.html'
	objeto = Banho.objects.get(id=pk)
	if request.method =='GET':
		form = BanhoForm(instance=objeto)
		return render(request, template_name, {'form':form})
	elif request.method=='POST':
		form = BanhoForm(request.POST, instance=objeto)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:banho_list'))
		else:
			return render(request, template_name, {'form': form})
# Listar os banhos cadastrados
def banho_list(request):
	template_name = 'banho/banho_list.html'
	obj = Banho.objects.all()
	return render(request, template_name, {'form': obj})
# Deletar um banho
def banho_delete(request, pk):
	template_name = 'banho/banho_delete.html'
	objeto = Banho.objects.get(id=pk)
	if request.method == 'GET':
		return render(request, template_name, {'form': objeto})
	elif request.method == 'POST':
		objeto.delete()
		return HttpResponseRedirect(reverse('services:banho_list'))

def tosa_add(request):
	template_name = 'tosa/tosa_add.html'
	if request.method == 'GET':
		form = TosaForm()
		return render(request, template_name, {'form':form})
	elif request.method == 'POST':
		form = TosaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:tosa_list'))
		else:
			return render(request, template_name, {'form':form})
def tosa_update(request, pk):
	template_name ='tosa/tosa_update.html'
	objeto = Tosa.objects.get(id=pk)
	if request.method =='GET':
		form = TosaForm(instance=objeto)
		return render(request, template_name, {'form':form})
	elif request.method=='POST':
		form = TosaForm(request.POST, instance=objeto)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:tosa_list'))
		else:
			return render(request, template_name, {'form': form})
def tosa_list(request):
	template_name = 'tosa/tosa_list.html'
	obj = Tosa.objects.all()
	return render(request, template_name, {'form': obj})
def tosa_delete(request, pk):
	template_name = 'tosa/tosa_delete.html'
	objeto = Tosa.objects.get(id=pk)
	if request.method == 'GET':
		return render(request, template_name, {'form': objeto})
	elif request.method == 'POST':
		objeto.delete()
		return HttpResponseRedirect(reverse('services:tosa_list'))

def itens_add(request):
	template_name = 'itens/itens_add.html'
	if request.method == 'GET':
		form = ItensForm()
		return render(request, template_name, {'form':form})
	elif request.method == 'POST':
		form = ItensForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:itens_list'))
		else:
			return render(request, template_name, {'form':form})
def itens_update(request, pk):
	template_name ='itens/itens_update.html'
	objeto = Itens.objects.get(id=pk)
	if request.method =='GET':
		form = ItensForm(instance=objeto)
		return render(request, template_name, {'form':form})
	elif request.method=='POST':
		form = ItensForm(request.POST, instance=objeto)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:itens_list'))
		else:
			return render(request, template_name, {'form': form})
def itens_list(request):
	template_name = 'itens/itens_list.html'
	obj = Itens.objects.all()
	return render(request, template_name, {'form': obj})
def itens_delete(request, pk):
	template_name = 'itens/itens_delete.html'
	objeto = Itens.objects.get(id=pk)
	if request.method == 'GET':
		return render(request, template_name, {'form': objeto})
	elif request.method == 'POST':
		objeto.delete()
		return HttpResponseRedirect(reverse('services:itens_list'))

def new_ficha(request, pk):
	template_name='ficha/new_ficha.html'
	pet = Pet.objects.get(id=pk)
	context={}
	niver = pet.aniversario
	age = int(birthday(niver))
	
	if request.method == 'GET':
		form = FichaForm()
		form_pet_factory = inlineformset_factory(Pet, Ficha, form=FichaForm, extra=1, can_delete=False)
		form_pet = form_pet_factory(instance=pet)
		if age >= 0:
			context['msg'] = 'anos'
		else:
			context['msg'] = 'meses'
		context = {
			'form': form_pet,
			'pet': pet,
			
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = FichaForm(request.POST)

		form_pet_factory = inlineformset_factory(Pet, Ficha, form=FichaForm, extra=1, can_delete=False)
		form_pet = form_pet_factory(request.POST, instance=pet)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={'pk': pk}))
		else:
			context = {
				'form': form_pet,
				'pet': pet,
				
			}
			return render(request, template_name, context=context)
