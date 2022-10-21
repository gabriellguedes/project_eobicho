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
from .models import Profile, Endereco
from .forms import ProfileForm, ProfileUpdateForm, EnderecoForm, LoginForm, UserRegistrationForm, UserEditForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

# Novo Cliente(Cadastro Feito pelo próprio cliente)
def new_client(request):
	template_name='accounts/register.html'
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
			assign_role(new_user, 'cliente')
			user = authenticate(username=new_user.username, password=request.POST['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': new_user.id}))
			else:
				return 'Deu erro!'
		
		else:
			context = {'form': form}
			return render(request, template_name, context=context)

# Registro Cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission') 
def user_add(request):
	template_name = 'accounts/user_add.html'
	if request.method == 'GET':
		user_form = UserRegistrationForm()
		form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory()
		context = {
			'form_user':user_form,
			'form_cliente': form_cliente,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)

		form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileForm, extra=1, can_delete=False)
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
			if request.POST['profile_set-0-cargo'] == 'Gerente':
				assign_role(new_user, 'gerente')
			elif request.POST['profile_set-0-cargo'] == 'MedicoVet':
				assign_role(new_user, 'medicovet')
			elif request.POST['profile_set-0-cargo'] == 'Colaborador':
				assign_role(new_user, 'colaborador')
			else:
				assign_role(new_user, 'cliente')	
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

# Listar Clientes
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('is_funcionario', redirect_to_login='core:permission')
def user_list(request):
	template_name = 'accounts/user_list.html'
	if request.user.is_authenticated:
		user = request.user
	else:
		user = ''

	obj_users = User.objects.all()

	parametro_page = request.GET.get('page', '1')
	parametro_limit = request.GET.get('limit', '5')

	if not (parametro_limit.isdigit() and int(parametro_limit)>0):
		parametro_limit = '10'

	clientes = User.objects.get_queryset().order_by('id')
	clientes_paginator = Paginator(clientes, parametro_limit)

	lista = User.objects.all()
	profile = Profile.objects.all()
	try:
		page = clientes_paginator.page(parametro_page)

	except (EmptyPage, PageNotAnInteger):
		page = clientes_paginator.page(1)


	context = {
		'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'clientes': page,
		'lista': lista,
		'user': user,
		'profile': profile,
	}
	return render(request, template_name, context=context)

# Detail CLiente acesso pelo admin
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def user_detail_admin(request, pk):
	template_name = 'accounts/user_detail.html'
	user = User.objects.get(id=pk)
	try:
		cliente = Profile.objects.get(user=user)
	except ObjectDoesNotExist:
		cliente = ''	
	pet = Pet.objects.filter(tutor=user.id)
	pet_last = pet.last()

	context = {
		'cliente': cliente,
		'user': user,
		'pet': pet,
	}
	return render(request, template_name, context=context)

# Detail Cliente acesso pelo cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def user_detail(request, pk):
	template_name = 'accounts/user_detail.html'
	user = request.user
	
	try:
		cliente = Profile.objects.get(user=user)
	except ObjectDoesNotExist:
		cliente =''

	try:
		endereco = Endereco.objects.get(user=cliente)
	except (ObjectDoesNotExist, ValueError):
		endereco = ''

	pet = Pet.objects.filter(tutor=user)
	pet_last = pet.last()

	context = {
		'cliente': cliente,
		'endereco': endereco,
		'user': user,
		'pet': pet,
	}
	return render(request, template_name, context=context)

# Atualização Cliente Feita pelo Cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('update_user_cliente')
def user_update(request, pk):
    template_name = 'accounts/user_update.html'
    if request.user.is_authenticated:
    	user = request.user

    obj = User.objects.get(id=pk)
    obj_profile = Profile.objects.get(user=obj)

    try:
        cliente =  Profile.objects.get(user=obj)
        if cliente != None:
            a = 0
        else:
            a = 1
    except ObjectDoesNotExist:
        a = 1

    try:
        endereco = Endereco.objects.get(user=obj_profile)
        if  endereco != None:
            b = 0 
        else:
            b = 1
    except ObjectDoesNotExist:
        b =1   


    if request.method == 'GET':
    	user_form = UserEditForm(instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileUpdateForm, extra=a, can_delete=False)
    	form_cliente = form_cliente_factory(instance=obj)

    	form_endereco_factory = inlineformset_factory(Profile, Endereco, form=EnderecoForm, extra=b, can_delete=False)
    	form_endereco = form_endereco_factory(instance=obj_profile)

    	context = {
    		'user_form': user_form,
    		'profile_form': form_cliente,
    		'endereco': form_endereco,
    		'cliente': user,
    		
    	}
    	return render(request, template_name, context=context)
    elif request.method == 'POST':
    	user_form = UserEditForm(request.POST,instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileUpdateForm, can_delete=False)
    	form_cliente = form_cliente_factory(request.POST, request.FILES, instance=obj)
    	
    	form_endereco_factory = inlineformset_factory(Profile, Endereco, form=EnderecoForm, extra=a, can_delete=False)
    	form_endereco = form_endereco_factory(request.POST ,instance=obj_profile)

    	if user_form.is_valid() and form_cliente.is_valid() and form_endereco.is_valid():
    		edit_user = user_form.save()
    		form_cliente.instance = edit_user 
    		profile = form_cliente.save()
    		print(profile)
    	
    		form_endereco.save()
    		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': pk}))
    	else:
    		context = {
    			'user_form': user_form,
    			'profile_form': form_cliente,
    			'endereco': form_endereco,
    			'cliente': user,
    			
    		}
    		print('Deu erro!')
    		return render(request,  template_name, context=context)

# Atualização Cliente Feito por Adm ou Gerente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('update_user_cliente')
def user_update_for_adm(request, pk):
    template_name = 'accounts/user_update.html'
    if request.user.is_authenticated:
    	user = request.user

    obj = User.objects.get(id=pk)
    obj_profile = Profile.objects.get(user=obj)

    try:
        cliente =  Profile.objects.get(user=obj)
        if cliente != None:
            a = 0
        else:
            a = 1
    except ObjectDoesNotExist:
        a = 1

    try:
        endereco = Endereco.objects.get(user=obj_profile)
        if  endereco != None:
            b = 0 
        else:
            b = 1
    except ObjectDoesNotExist:
        b =1   


    if request.method == 'GET':
    	user_form = UserEditForm(instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileForm, extra=a, can_delete=False)
    	form_cliente = form_cliente_factory(instance=obj)

    	form_endereco_factory = inlineformset_factory(Profile, Endereco, form=EnderecoForm, extra=b, can_delete=False)
    	form_endereco = form_endereco_factory(instance=obj_profile)

    	context = {
    		'user_form': user_form,
    		'profile_form': form_cliente,
    		'endereco': form_endereco,
    		'cliente': user,
    		
    	}
    	return render(request, template_name, context=context)
    elif request.method == 'POST':
    	user_form = UserEditForm(request.POST,instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileForm)
    	form_cliente = form_cliente_factory(request.POST, request.FILES, instance=obj)
    	
    	form_endereco_factory = inlineformset_factory(Profile, Endereco, form=EnderecoForm, extra=a, can_delete=False)
    	form_endereco = form_endereco_factory(request.POST ,instance=obj_profile)

    	if user_form.is_valid() and form_cliente.is_valid() and form_endereco.is_valid():
    		edit_user = user_form.save()
    		form_cliente.instance = edit_user 
    		profile = form_cliente.save()
    		print(profile)
    	
    		form_endereco.save()
    		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': pk}))
    	else:
    		context = {
    			'user_form': user_form,
    			'profile_form': form_cliente,
    			'endereco': form_endereco,
    			'cliente': user,
    			
    		}
    		print('Deu erro!')
    		return render(request,  template_name, context=context)

#Apagar Cliente   
class user_delete(LoginRequiredMixin, DeleteView):
	login_url= reverse_lazy('core:home')
	template_name = 'accounts/user_delete.html'
	queryset = User.objects.all()
	success_url = reverse_lazy('contas:cliente_list')

