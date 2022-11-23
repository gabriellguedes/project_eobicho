from django.shortcuts import render, redirect
from ecommerce.pet.tuplas import Tuplas
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from ecommerce.pet.models import Pet
from .models import Profile, Endereco, Cargo
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from rolepermissions.roles import assign_role, clear_roles
from rolepermissions.permissions import revoke_permission
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from django.core.mail import send_mail
from ecommerce.core.views import newsletter_add
tuplas = Tuplas()
# Novo Cliente(Cadastro Feito pelo próprio cliente)
def new_client(request):
	template_name='accounts/register.html'
	context={}
	if request.method == 'GET':
		form = UserRegistrationForm()
		form_cargo_factory = inlineformset_factory(User, Cargo, form=ChangeCargoForm, extra=1, can_delete=False)
		form_cargo = form_cargo_factory()
		context = {
			'form': form,
			'form_cargo': form_cargo,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		form_cargo_factory = inlineformset_factory(User, Cargo, form=ChangeCargoForm, extra=1, can_delete=False)
		form_cargo = form_cargo_factory(request.POST)
		# Condição de tamanho da senha
		if len(request.POST['password']) < 6:
			context['msg'] = 'Senha deve conter no mínimo 6 caracteres.'
			context['class'] = 'alert alert-info'
			return render(request, template_name, context=context)
		#Validando Formulários
		if form.is_valid() and form_cargo.is_valid():
			try:
				new_user = form.save(commit=False)
				new_user.set_password(form.cleaned_data['password'])
				new_user.username = new_user.email				
				new_user.save()
				#Adicionando Cargo Cliente
				form_cargo.instance = new_user
				new_cargo = form_cargo.save()

				if request.POST.get('email_market', False):
					nome = new_user.first_name
					email = new_user.email
					newsletter_add(nome, email)
				else:
					pass
				assign_role(new_user, 'cliente')
				user = authenticate(username=new_user.username, password=request.POST['password'])
				if user is not None:
					login(request, user)
					return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': new_user.id}))
				else:
					form = UserRegistrationForm()
					context = {
						'form': form,
						'form_cargo': form_cargo,
						'msg': 'Algo deu errado!',
						'class': 'alert alert-primary',
					}
					return render(request, template_name, context=context)
			except IntegrityError:
				form = UserRegistrationForm()
				context = {
					'form': form,
					'form_cargo': form_cargo,
					'msg': 'Email já cadastrado.',
					'class': 'alert alert-warning',
				}
				return render(request, template_name, context=context)
		else:
			context = {
				'form': form,
				'msg': 'Usuário não foi cadastrado!',
				'class': 'alert alert-warning',
			}
			return render(request, template_name, context=context)
# Registro Novo Usuário
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission') 
def user_add(request):
	template_name = 'accounts/user_add.html'
	if request.method == 'GET':
		user_form = UserRegistrationForm()
		form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory()

		form_cargo_factory = inlineformset_factory(User, Cargo, form=ChangeCargoForm, extra=1, can_delete=False)
		form_cargo = form_cargo_factory()
		context = {
			'form_user':user_form,
			'form_cliente': form_cliente,
			'form_cargo': form_cargo,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)

		form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory(request.POST, request.FILES)

		form_cargo_factory = inlineformset_factory(User, Cargo, form=ChangeCargoForm, extra=1, can_delete=False)
		form_cargo = form_cargo_factory(request.POST)
		context ={}
		# validando formulários
		if user_form.is_valid() and form_cliente.is_valid() and form_cargo.is_valid():
			new_user = user_form.save()
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.username = new_user.email
			new_user.save()

			form_cargo.instance = new_user
			form_cargo.save()

			if request.POST['cargo-0-cargo'] == 'Gerente':
				assign_role(new_user, 'gerente')
			elif request.POST['cargo-0-cargo'] == 'Medico Veterinario':
				assign_role(new_user, 'medico')
			elif request.POST['cargo-0-cargo'] == 'Colaborador':
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
					'msg': 'Erro: Cliente não cadastrado!',
					'class': 'alert alert-danger',
				}
			return render(request, 'site/block-cadastro.html', context=context)	
# Registro Cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission') 
def cliente_add(request):
	template_name = 'accounts/new_cliente_add.html'
	context={}
	if request.method == 'GET':
		form = UserRegistrationForm()
		form_cliente_factory = inlineformset_factory(User, Profile, form=ClienteAddForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory()
		form_cargo_factory = inlineformset_factory(User, Cargo, form=ChangeCargoForm, extra=1, can_delete=False)
		form_cargo = form_cargo_factory()
		context = {
			'form': form,
			'form_user': form_cliente,
			'form_cargo': form_cargo,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		form_cliente_factory = inlineformset_factory(User, Profile, form=ClienteAddForm, extra=1, can_delete=False)
		form_cliente = form_cliente_factory(request.POST)
		form_cargo_factory = inlineformset_factory(User, Cargo, form=ChangeCargoForm, extra=1, can_delete=False)
		form_cargo = form_cargo_factory(request.POST)
		if form.is_valid() and form_cliente.is_valid() and form_cargo.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.username = new_user.email
			new_user.save()
			
			form_cargo.instance = new_user
			form_cargo.save()

			form_cliente.instance = new_user
			new_cliente = form_cliente.save()
			
			assign_role(new_user, 'cliente')
			return HttpResponseRedirect(reverse('contas:cliente_list'))
		else:
			context['form'] = form
			context['form_user'] = form_cliente
			context['msg'] = 'Algo deu errado! Cliente não foi cadastrado.'
			context['class'] = 'alert alert-warning'
			return render(request, template_name, context=context)
# Listar Todos os Clientes Cadastrados no Sistema
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
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
# Visualizar Dados do cliente	
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def user_profile(request, pk):
	template_name = 'accounts/user_profile.html'
	user = User.objects.get(id=pk)
	try:
		profile = Profile.objects.get(user=user)
	except ObjectDoesNotExist:
		profile = ''
	try:
		endereco = Endereco.objects.get(user=user)
	except ObjectDoesNotExist:
		endereco = ''
	context = {
		'cliente': user,
		'profile': profile,
		'endereco': endereco,
	}
	return render(request, template_name, context=context)
# Detail Cliente acesso pelo cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def user_detail(request, pk):
	template_name = 'accounts/user_detail.html'
	context={}
	user = request.user
	tutor = User.objects.get(id=pk)

	#send_mail('Django teste', 'Este é um email teste', 'lojamyitens@gmail.com', ['gguedes10@gmail.com'])

	try:
		cliente = Profile.objects.get(user=user)
	except ObjectDoesNotExist:
		cliente = 'None'

	try:		
		endereco = Endereco.objects.get(user=user)
	except (ObjectDoesNotExist, ValueError):
		endereco = 'None'		
	
	pet_cliente = Pet.objects.filter(tutor=tutor)

	pet = Pet.objects.filter(tutor=user)
	pet_last = pet.last()

	context = {
		'cliente': cliente,
		'endereco': endereco,
		'user': user,
		'pet': pet,
		'tutor': tutor,
		'pet_cliente': pet_cliente,
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
   
    try:
        cliente =  Profile.objects.get(user=obj)
        if cliente != None:
            a = 0
        else:
            a = 1
    except ObjectDoesNotExist:
        a = 1

    try:
        endereco = Endereco.objects.get(user=obj)
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
    	form_endereco_factory = inlineformset_factory(User, Endereco, form=EnderecoForm, extra=b, can_delete=False)
    	form_endereco = form_endereco_factory(instance=obj)

    	context = {
    		'user_form': user_form,
    		'profile_form': form_cliente,
    		'endereco': form_endereco,
    		'cliente': obj,
    		
    	}
    	return render(request, template_name, context=context)
    elif request.method == 'POST':
    	user_form = UserEditForm(request.POST,instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileUpdateForm, can_delete=False)
    	form_cliente = form_cliente_factory(request.POST, request.FILES, instance=obj)
    	form_endereco_factory = inlineformset_factory(User, Endereco, form=EnderecoForm, extra=a, can_delete=False)
    	form_endereco = form_endereco_factory(request.POST ,instance=obj)

    	if user_form.is_valid() and form_cliente.is_valid() and form_endereco.is_valid():
    		edit_user = user_form.save(commit=False)
    		form_cliente.instance = edit_user 
    		edit_user.save()
    		form_cliente.save()
    		form_endereco.save()
    		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': pk}))
    	else:
    		context = {
    			'user_form': user_form,
    			'profile_form': form_cliente,
    			'endereco': form_endereco,
    			'cliente': obj,
    			
    		}
    		return render(request,  template_name, context=context)
# Atualização Cliente Feito por Adm ou Gerente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('update_user')
def user_update_for_adm(request, pk):
    template_name = 'accounts/user_update.html'
    if request.user.is_authenticated:
    	user = request.user

    obj = User.objects.get(id=pk)

    try:
        cliente =  Profile.objects.get(user=obj)
        if cliente != None:
            a = 0
        else:
            a = 1
    except ObjectDoesNotExist:
        a = 1

    try:
        endereco = Endereco.objects.get(user=obj)
        if  endereco != None:
            b = 0 
        else:
            b = 1
    except ObjectDoesNotExist:
        b =1   


    if request.method == 'GET':
    	user_form = UserEditForm(instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileUpdateFullForm, extra=a, can_delete=False)
    	form_cliente = form_cliente_factory(instance=obj)

    	form_endereco_factory = inlineformset_factory(User, Endereco, form=EnderecoForm, extra=b, can_delete=False)
    	form_endereco = form_endereco_factory(instance=obj)

    	context = {
    		'user_form': user_form,
    		'profile_form': form_cliente,
    		'endereco': form_endereco,
    		'cliente': obj,
    		
    	}
    	return render(request, template_name, context=context)
    elif request.method == 'POST':
    	user_form = UserEditForm(request.POST,instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileUpdateFullForm, can_delete=False)
    	form_cliente = form_cliente_factory(request.POST, request.FILES, instance=obj)
    	
    	form_endereco_factory = inlineformset_factory(User, Endereco, form=EnderecoForm, extra=a, can_delete=False)
    	form_endereco = form_endereco_factory(request.POST ,instance=obj)

    	if user_form.is_valid() and form_cliente.is_valid() and form_endereco.is_valid():
    		edit_user = user_form.save()
    		form_cliente.instance = edit_user 
    		profile = form_cliente.save()
    	
    		form_endereco.save()
    		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': pk}))
    	else:
    		context = {
    			'user_form': user_form,
    			'profile_form': form_cliente,
    			'endereco': form_endereco,
    			'cliente': obj,
    			
    		}
    		return render(request,  template_name, context=context)
#Apagar Cliente   
def user_delete(request, pk):
	template_name = 'accounts/user_delete.html'
	objeto = User.objects.get(id=pk)
	if request.method == 'GET':
		context = {'cliente': objeto,}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		objeto.delete()
		return HttpResponseRedirect(reverse('contas:cliente_list'))

#Alterarar cargo do usuário
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def change_cargo(request, pk):
	template_name = 'accounts/change_cargo.html'
	objeto = User.objects.get(id=pk)
	if request.method == 'GET':	
		form_change_factory = inlineformset_factory(User, Cargo, form = ChangeCargoForm, extra=1, can_delete=False)
		form_change = form_change_factory( instance=objeto)
		context = {
			'form':form_change, 
			'obj': objeto,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':		
		form_change_factory = inlineformset_factory(User, Cargo, form = ChangeCargoForm, extra=0, can_delete=False)
		form_change = form_change_factory(request.POST, instance=objeto )
		try:
			if form_change.is_valid():
				clear_roles(objeto)
				form_change.instance = objeto
				# adicionando permissões
				if request.POST['cargo-0-cargo'] == 'Gerente':
					assign_role(objeto, 'gerente')
				elif request.POST['cargo-0-cargo'] == 'Medico Veterinario':
					assign_role(objeto, 'medico')
				elif request.POST['cargo-0-cargo'] == 'Colaborador':
					assign_role(objeto, 'colaborador')
				else:
					assign_role(objeto, 'cliente')
				form_change.save()
				return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': pk}))
		except ObjectDoesNotExist:
			form_change_factory = inlineformset_factory(User, Cargo, form = ChangeCargoForm, extra=0, can_delete=False)
			form_change = form_change_factory(request.POST)
			if form_change.is_valid():
				form_change.instance = objeto
				form_change.save()
				assign_role(objeto, 'cliente')
				return HttpResponseRedirect(reverse('contas:change_cargo', pk=objeto.id))
			else:
				context = {
					'msg': 'Não foi possível adicionar o usuário ao grupo cliente. Entre em contato com o Administrador do sistema.',
					'class': 'alert alert-danger',
				}
				return render(request, template_name, context=context)	
		else:
			context = {
				'msg':'Algo deu errado! Alteração não realizada.',
				'class':'alert alert-danger',
				'form':form_change,
				'obj': objeto,
			}
			return render(request, template_name, context=context)

# Adicionar um pet já existem ao tutor 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def tutor_add(request, pk):
	template_name = 'accounts/tutor_add.html'
	tutor = User.objects.get(id=pk)
	context = {'tutor': tutor,}
	if request.method == 'GET':
		return render(request,template_name, context=context)
	elif request.method == 'POST':
		try:
			obj = request.POST['idPetcadastrado']
			pet = Pet.objects.get(id=obj)
			tutor.tutores.add(pet)
		except ValueError:
			context['msg'] = 'O Id do Pet é composto apenas por números.'
			context['class'] = 'alert alert-info'
			return render(request, template_name, context=context)
		except ObjectDoesNotExist:
			context['msg'] = 'Id não existe!'
			context['class'] = 'alert alert-info'
			return render(request, template_name, context=context)
		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': tutor.id }))
# Remover um pet já existem ao tutor 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def tutor_remove(request, pk, n):
	template_name = 'accounts/tutor_remove.html'
	tutor = User.objects.get(id=pk)
	pet = Pet.objects.get(id=n)
	if request.method == 'GET':
		context = { 
			'pet': pet,
			'tutor': tutor,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		tutor.tutores.remove(pet)
		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': pk}))
# Adicionar um tutor ao pet
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pet_add_tutor(request, pk):
	template_name ='accounts/pet_add_tutor.html'
	pet = Pet.objects.get(id=pk)
	context = {'pet':pet}
	if request.method == 'GET':
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		try:
			obj = request.POST['idTutorCadastrado']
			tutor = User.objects.get(id=obj)
			tutor.tutores.add(pet)
		except ValueError:
			context['msg'] = 'O Id do Tutor é composto apenas por números.'
			context['class'] = 'alert alert-info'
			return render(request, template_name, context=context)
		except ObjectDoesNotExist:
			context['msg'] = 'Id não existe!'
			context['class'] = 'alert alert-info'
			return render(request, template_name, context=context)
		return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={'pk': pk }))
