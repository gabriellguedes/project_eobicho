
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from ecommerce.pet.models import Pet
from .models import Cliente, Funcionario
from .forms import ClienteForm, FuncionarioForm

def home(request):
	template_name = 'accounts/home.html'
	
	return render(request,template_name)

# Add Cliente 
def cliente_add(request):
	template_name = 'clientes/cliente_add.html'
	form = ClienteForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('contas:cliente_list'))
	context = {'form': form	}
	return render(request, template_name, context=context)

# Listar Cliente
def cliente_list(request):
	template_name = 'clientes/cliente_list.html'
	parametro_page = request.GET.get('page', '1')
	parametro_limit = request.GET.get('limit', '5')

	if not (parametro_limit.isdigit() and int(parametro_limit)>0):
		parametro_lim

	clientes = Cliente.objects.get_queryset().order_by('id')
	clientes_paginator = Paginator(clientes, parametro_limit)

	lista = Cliente.objects.all()

	try:
		page = clientes_paginator.page(parametro_page)

	except (EmptyPage, PageNotAnInteger):
		page = clientes_paginator.page(1)


	context = {
		'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'clientes': page,
		'lista': lista,
	}
	return render(request, template_name, context=context)

# Detail CLiente
def cliente_detail(request, pk):
	template_name = 'clientes/cliente_detail.html'
	obj_cliente = Cliente.objects.get(id=pk)
	pet = Pet.objects.filter(tutor=obj_cliente.id)
	pet_last = pet.last()

	context = {
		'cliente': obj_cliente,
		'pet': pet,
	}
	return render(request, template_name, context=context)

# Atualização Cliente
class cliente_update(UpdateView):
    template_name = 'clientes/cliente_update.html'
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('contas:cliente_list')

#Apagar Cliente   
class cliente_delete(DeleteView):
	template_name = 'clientes/cliente_delete.html'
	queryset = Cliente.objects.all()
	success_url = reverse_lazy('contas:cliente_list')

# Add Funcionário
def funcionario_add(request):
	template_name = 'funcionarios/funcionario_add.html'
	if request.method == 'GET':
		form = FuncionarioForm()
		context = {
			'form': form
		}	
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = FuncionarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('contas:funcionario_list'))
		else:		
			context = {
			'form': form
			}	
			return render(request, template_name, context=context)

#Detail funcionario
def funcionario_detail(request, pk):
	template_name = 'funcionarios/funcionario_detail.html'
	obj_funcionario = Funcionario.objects.get(id=pk)

	context = { 'funcionario': obj_funcionario,}
	return render(request, template_name, context=context)

# Lista de todos os funcionários
def funcionario_list(request):
	template_name = 'funcionarios/funcionario_list.html'
	parametro_page = request.GET.get('page', '1')
	parametro_limit = request.GET.get('limit', '5')

	if not (parametro_limit.isdigit() and int(parametro_limit)>0):
		parametro_lim

	funcionarios = Cliente.objects.get_queryset().order_by('id')
	funcionarios_paginator = Paginator(funcionarios, parametro_limit)

	objeto = Funcionario.objects.all()

	try:
		page = funcionarios_paginator.page(parametro_page)

	except (EmptyPage, PageNotAnInteger):
		page = funcionarios_paginator.page(1)

	context= {
		'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'funcionarios': page,
		'form': objeto,
	}
	return render(request, template_name, context=context)

# Atualizar Funcionário
def funcionario_update(request, pk):
	template_name = 'funcionarios/funcionario_update.html'
	objeto = Funcionario.objects.get(id=pk)
	
	if request.method == 'GET':
		form = FuncionarioForm(instance=objeto)
		context = { 'form': form}
		return render(request, template_name, context=context)

	elif request.method == 'POST':
		form = FuncionarioForm(request.POST, instance=objeto)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('contas:funcionario_list'))
		else:
			context = {
				'form': form
			}
			return render(request, template_name, context=context)

# Deletar Funcionário
class funcionario_delete(DeleteView):
	template_name = 'funcionarios/funcionario_delete.html'
	queryset = Funcionario.objects.all()
	success_url = reverse_lazy('contas:funcionario_list')

