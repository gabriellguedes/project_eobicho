
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from ecommerce.pet.models import Pet
from .models import Cliente, Funcionario
from .forms import ClienteForm, FuncionarioForm, LoginForm, UserRegistrationForm, UserEditForm, ClienteEditForm


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
def cliente_update(request, pk):
    template_name = 'clientes/cliente_update.html'
    obj = Cliente.objects.get(id=pk)
    pet = Pet.objects.get(tutor=obj)
    if request.method == 'GET':
    	form = ClienteForm(instance=obj)
    	context = {'form': form,'pet': pet}
    	return render(request, template_name, context=context)
    elif request.method == 'POST':
    	form = ClienteForm(request.POST, request.FILES, instance=obj)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect(reverse('contas:cliente_list'))
    	else:
    		context = {'form': form, 'pet': pet,}
    		return render(request, template_name, context=context)
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

#Registro Cliente 
def cliente_add(request):
	template_name = 'accounts/register.html'
	if request.method == 'GET':
		user_form = UserRegistrationForm()
		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteEditForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory()
		context = {
			'form_user':user_form,
			'form_cliente': form_cliente,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		user_form = UserRegistrationForm(request.POST, request.FILES)
		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteEditForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory(request.POST, request.FILES)
		context ={}
		
		if user_form.is_valid() and form_cliente.is_valid():
		# Create a new user object but avoid saving it yet
			new_user = user_form.save()
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.username = new_user.email
			# Save the User object
			new_user.save()
			# Create the user profile
			form_cliente.instance = new_user
			form_cliente.save()
			return render(request, 'accounts/register_done.html')
		else:
			if user_form.is_valid():
				new_user = user_form.save()
				# Set the chosen password
				new_user.set_password(user_form.cleaned_data['password'])
				new_user.username = new_user.email
				# Save the User object
				new_user.save()
				
			context = {
				'user_form': user_form,
				'form_cliente': form_cliente,
				'msg': 'Erro: Cliente não cadastrado',
				'class': 'alert alert-danger',
			}
			return render(request, template_name, context=context)
#Editar Usuário
def edit(request):
	template_name = 'accounts/edit.html'
	if request.method == 'GET':
		user_form = UserEditForm(instance=request.user)

		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteEditForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory(instance=request.user)
		context = {
			'user_form': user_form,
			'profile_form': form_cliente
		}
		return render(request, template_name, context=context)


	elif request.method == 'POST':
		user_form = UserEditForm(request.POST,instance=request.user)
		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteEditForm)
		form_cliente = form_cliente_factory(request.POST, request.FILES, instance=request.user)
		
		if user_form.is_valid() and form_cliente.is_valid():
			edit_user = user_form.save()
			form_cliente.instance = edit_user
			form_cliente.save()
			return HttpResponseRedirect(reverse('contas:cliente_list'))
		else:
			context = {
				'user_form': user_form,
				'profile_form': form_cliente
			}
			return render(request,  template_name, context=context)

