from django.shortcuts import render, resolve_url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from ecommerce.accounts.models import Profile
from ecommerce.accounts.forms import ProfileForm, UserRegistrationForm, UserEditForm
from ecommerce.core.models import TimeStampedModel
from ecommerce.core.forms import TimeStampedForm
from ecommerce.ficha.models import Ficha
from ecommerce.ficha.peso.models import Peso
from ecommerce.ficha.forms import FichaForm
from ecommerce.ficha.peso.forms import PesoForm
from ecommerce.ficha.especie.models import Especie
from ecommerce.ficha.raca.models import Raca
from .forms import PetForm
from .models import Pet
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from PIL import Image

@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pet_add(request):
    template_name = 'pet/pet_add.html'
    especie = Especie.objects.all().order_by('especie')
    raca = []

    if request.method == 'GET':
        form = PetForm()
        context = {
            'form': form,
            'especie': especie,
            'raca': raca,
            }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pet:pet_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)

#Cadastro Pet feito pelo cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def cliente_pet_add(request, pk):
    template_name = 'pet/cliente_pet_add.html'
    obj = request.user
    especie = Especie.objects.all().order_by('especie')
    raca = []

    if request.method == 'GET':
        form = UserRegistrationForm()

        form_pet_factory = inlineformset_factory(User, Pet, form=PetForm, extra=1)
        form_pet = form_pet_factory()

        context = {
            'especie': especie,
            'raca': raca,
            'form': form_pet,
            'cliente': obj,
        }
        return render(request, template_name, context=context)

    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        form_pet_factory = inlineformset_factory(User, Pet, form=PetForm)
        form_pet = form_pet_factory(request.POST, request.FILES)
               
        if form_pet.is_valid():
            form_pet.instance = obj
            form_pet.save()

            return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={"pk": obj.pk}))
        else:
            context = {
                'especie': especie,
                'raca': raca,
                'form': form_pet,
                'cliente': obj,
            }
            return render(request, template_name, context=context)
#Lista de Exibição Paginação
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def paginacao(request):
    template_name = 'pet/pet_list.html'
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '5')
    
    if not (parametro_limit.isdigit() and int(parametro_limit)>0):
        parametro_limit = '10'

    pets = Pet.objects.get_queryset().order_by('id')
    pets_paginator = Paginator(pets, parametro_limit)

    objects = Pet.objects.all()
    
  
    try:
        page = pets_paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = pets_paginator.page(1)
       

    context = {
        'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'pets': page,
        'object_list':objects
    }
    return render(request, template_name, context=context)
#Vizualizar Pet e Ficha
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def detailPet(request, pk):
    template_name ='pet/pet_detail.html'
    
    obj = Pet.objects.get(id=pk)
    ficha = obj.fichaPets.last()
    last_fichas = obj.fichaPets.all()
    tutor = obj.tutor.id
    obj_cliente = User.objects.get(id=tutor)
    
    # Listar Peso        
    list_peso = Peso.objects.filter(pet=obj)
    last_peso = list_peso.last()    
    
   
   
    context = { 
        'pet': obj,
        'ficha': ficha,
        'last_fichas': last_fichas,
        'last_peso': last_peso,
        'listpeso': list_peso,
        'cliente': obj_cliente,
     }
    return render(request, template_name, context=context) 
#Atualização
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pet_update(request, pk):
    template_name = 'pet/pet_update.html'
    obj = Pet.objects.get(id=pk)
    especie = Especie.objects.all().order_by('especie')
    raca = []

    if request.method == 'GET':
        form = PetForm(instance=obj)
        context = {
            'form_pet': form,
            'especie': especie,
            'raca': raca,
        }
        return render(request, template_name, context=context)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=obj)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={"pk": obj.pk}))
        else:
            context = { 
                'form_pet': form,
                'especie': especie,
                'raca': raca
            }
            return render(request, template_name, context=context)

#Select Espécie e Raça Add Pet por um funcionário
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def load_funcoes(request):
    template_name = 'pet/funcao_ajax.html'
    especie_id = request.GET.get('id_especie')
    raca = Raca.objects.filter(especie=especie_id)
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)
# Select Espécie e Raça Add Pet por um Cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def load_cliente(request):
    template_name = 'pet/cliente_ajax.html'
    especie_id = request.GET.get('id_pet_set-0-especie')
    raca = Raca.objects.filter(especie=especie_id)
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)
# Select Espécie e Raça Add Pet por um Cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def load_update_pet(request):
    template_name = 'pet/update_pet_ajax.html'
    especie_id = request.GET.get('id_especie')
    raca = Raca.objects.filter(especie=especie_id)
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)
