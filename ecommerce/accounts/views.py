
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
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
from .forms import ClienteForm, FuncionarioForm, LoginForm, UserRegistrationForm, UserEditForm


# Listar Cliente
def cliente_list(request):
	template_name = 'clientes/cliente_list.html'
	if request.user.is_authenticated:
		user = request.user
	else:
		user = ''

	obj_users= User.objects.all()

	parametro_page = request.GET.get('page', '1')
	parametro_limit = request.GET.get('limit', '5')

	if not (parametro_limit.isdigit() and int(parametro_limit)>0):
		parametro_lim

	clientes = User.objects.get_queryset().order_by('id')
	clientes_paginator = Paginator(clientes, parametro_limit)

	lista = User.objects.all()

	try:
		page = clientes_paginator.page(parametro_page)

	except (EmptyPage, PageNotAnInteger):
		page = clientes_paginator.page(1)


	context = {
		'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'clientes': page,
		'lista': lista,
		'users': obj_users,
		'user': user,
	}
	return render(request, template_name, context=context)
# Detail CLiente acesso pelo admin
def cliente_detail_admin(request, pk):
	template_name = 'clientes/cliente_detail.html'
	user = User.objects.get(id=pk)
	cliente = Cliente.objects.get(user=user)

	pet = Pet.objects.filter(tutor=user.id)
	pet_last = pet.last()

	context = {
		'cliente': cliente,
		'user': user,
		'pet': pet,
	}
	return render(request, template_name, context=context)
# Detail Cliente acesso pelo cliente
def cliente_detail(request, pk):
	template_name = 'clientes/cliente_detail.html'
	user = request.user
	cliente = Cliente.objects.get(user=user)

	pet = Pet.objects.filter(tutor=user)
	pet_last = pet.last()

	context = {
		'cliente': cliente,
		'user': user,
		'pet': pet,
	}
	return render(request, template_name, context=context)
# Atualização Cliente
def cliente_update(request, pk):
    template_name = 'clientes/cliente_update.html'
    if request.user.is_authenticated:
    	user = request.user

    obj = User.objects.get(id=pk)
    try:
        cliente =  Cliente.objects.get(user=obj)
        if cliente != None:
            a = 0
        else:
            a = 1
    except ObjectDoesNotExist:
        a = 1


    if request.method == 'GET':
    	user_form = UserEditForm(instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteForm, extra=a, can_delete=False)
    	form_cliente = form_cliente_factory(instance=obj)
    	context = {
    		'user_form': user_form,
    		'profile_form': form_cliente,
    		'cliente': user,
    		
    	}
    	return render(request, template_name, context=context)
    elif request.method == 'POST':
    	user_form = UserEditForm(request.POST,instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteForm)
    	form_cliente = form_cliente_factory(request.POST, request.FILES, instance=obj)
    	if user_form.is_valid() and form_cliente.is_valid():
    		edit_user = user_form.save()
    		form_cliente.instance = edit_user
    		form_cliente.save()
    		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': pk}))
    	else:
    		context = {
    			'user_form': user_form,
    			'profile_form': form_cliente,
    			'cliente': user,
    			
    		}
    		return render(request,  template_name, context=context)
#Apagar Cliente   
class cliente_delete(DeleteView):
	template_name = 'clientes/cliente_delete.html'
	queryset = User.objects.all()
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

# Registro Cliente 
def cliente_add(request):
	template_name = 'accounts/register.html'
	if request.method == 'GET':
		user_form = UserRegistrationForm()
		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory()
		context = {
			'form_user':user_form,
			'form_cliente': form_cliente,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)

		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteForm, extra=1, can_delete=False)
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
			cliente = form_cliente.save()
			obj = cliente[0]
			return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={"pk": obj.id}))
		
		else:
			context = {
					'user_form': user_form,
					'form_cliente': form_cliente,
					'msg': 'Erro: Cliente não cadastrado',
					'class': 'alert alert-danger',
				}
			return render(request, 'site/block-cadastro.html', context=context)	

# Novo cliente
def cliente_new(request):
	template_name = 'accounts/edit.html'
	if request.user.is_authenticated:
		user = request.user

	if request.method == 'GET':
		user_form = UserEditForm(instance=request.user)

		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory(instance=request.user)
		context = {
			'user_form': user_form,
			'profile_form': form_cliente,
			'cliente': user,
		}
		return render(request, template_name, context=context)


	elif request.method == 'POST':
		user_form = UserEditForm(request.POST,instance=request.user)
		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteForm)
		form_cliente = form_cliente_factory(request.POST, request.FILES, instance=request.user)
		
		if user_form.is_valid() and form_cliente.is_valid():
			edit_user = user_form.save()
			form_cliente.instance = edit_user
			form_cliente.save()
			return HttpResponseRedirect(reverse('contas:cliente_list'))
		else:
			context = {
				'user_form': user_form,
				'profile_form': form_cliente,
				'cliente': user,
			}
			return render(request,  template_name, context=context)
# Editar Usuário
def edit(request):
	template_name = 'accounts/edit.html'
	if request.user.is_authenticated:
		user = request.user

	if request.method == 'GET':
		user_form = UserEditForm(instance=request.user)

		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteForm, extra=0, can_delete=False)
		form_cliente = form_cliente_factory(instance=request.user)
		context = {
			'user_form': user_form,
			'profile_form': form_cliente,
			'cliente': user,
		}
		return render(request, template_name, context=context)


	elif request.method == 'POST':
		user_form = UserEditForm(request.POST,instance=request.user)
		form_cliente_factory = inlineformset_factory(User, Cliente, form=ClienteForm)
		form_cliente = form_cliente_factory(request.POST, request.FILES, instance=request.user)
		
		if user_form.is_valid() and form_cliente.is_valid():
			edit_user = user_form.save()
			form_cliente.instance = edit_user
			form_cliente.save()
			return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': user.id}))
		else:
			context = {
				'user_form': user_form,
				'profile_form': form_cliente,
				'cliente': user,
			}
			return render(request,  template_name, context=context)

def user_new(request):
	template_name='site/block_cadastro.html'
	if request.method == 'GET':
		form = UserRegistrationForm()
		context = {'form': form}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.username = new_user.email
			new_user.save()

			user = authenticate(username=new_user.username, password=request.POST['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': new_user.id}))
			else:
				return 'Deu erro!'
			
			
			

		else:
			context = {'form': form}
			return render(request, template_name, context=context)
