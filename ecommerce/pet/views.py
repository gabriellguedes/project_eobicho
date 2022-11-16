import dateutil
import datetime
from datetime import datetime
from dateutil.relativedelta import *
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
from ecommerce.ficha.models import Anamnese
from ecommerce.ficha.peso.models import Peso
from ecommerce.ficha.forms import AnamneseForm
from ecommerce.ficha.peso.forms import PesoForm
from ecommerce.ficha.especie.models import Especie
from ecommerce.ficha.raca.models import Raca
from .forms import PetForm, PetClienteAddForm, PetUpdateForm, PetClienteUpdateForm
from .models import Pet
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from PIL import Image

def birthday(date):
    # Get the current date
    now = datetime.utcnow()
    now = now.date()
    context = {}
    # Get the difference between the current date and the birthday
    try:
        age = dateutil.relativedelta.relativedelta(now, datetime.strptime(date, '%Y-%m-%d').date())
    except TypeError:
        age = dateutil.relativedelta.relativedelta(now, date)
    age = age.months
    return age

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
        aniversario = request.POST['aniversario']
        idade = birthday(aniversario)
        if form.is_valid():
            new_pet = form.save(commit=False)
            new_pet.idade = idade
            new_pet.save()
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
        form = PetClienteAddForm()

        context = {
            'especie': especie,
            'raca': raca,
            'form': form,
            'cliente': obj,
        }
        return render(request, template_name, context=context)

    elif request.method == 'POST':
        form = PetClienteAddForm(request.POST, request.FILES)
        aniversario = request.POST['aniversario']
        idade = birthday(aniversario)
        if form.is_valid():
            new_pet = form.save(commit=False)
            new_pet.idade = idade
            new_pet.save()
            obj.tutores.add(new_pet)

            return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={"pk": obj.pk}))
        else:
            context = {
                'especie': especie,
                'raca': raca,
                'form': form,
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


    try:
        page = pets_paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = pets_paginator.page(1)
       

    context = {
        'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'pets': page,
        
    }
    return render(request, template_name, context=context)
#Vizualizar Pet e Ficha
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def detailPet(request, pk):
    template_name ='pet/pet_detail.html'
    
    pet = Pet.objects.get(id=pk)
    tutor = pet.tutor.all()
    ficha = pet.fichaPets.last()
    last_fichas = pet.fichaPets.all()
    #obj_cliente = User.objects.get(id=tutor)

    # Listar Peso        
    list_peso = Peso.objects.filter(pet=pet)
    last_peso = list_peso.last()    
    
    #Atualizar idade do pet
    aniversario = pet.aniversario
    idade = birthday(aniversario)
    if pet.idade != idade:
        pet.idade = idade
        pet.save()
   
    context = { 
        'pet': pet,
        'ficha': ficha,
        'last_fichas': last_fichas,
        'last_peso': last_peso,
        'listpeso': list_peso,
        'cliente': tutor,
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
        form = PetUpdateForm(instance=obj)
        context = {
            'form_pet': form,
            'obj': obj,
            'especie': especie,
            'raca': raca,
        }
        return render(request, template_name, context=context)
    if request.method == 'POST':
        form = PetUpdateForm(request.POST, request.FILES, instance=obj)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            form.save()
            return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={"pk": obj.pk}))
        else:
            context = { 
                'form_pet': form,
                'obj': obj,
                'especie': especie,
                'raca': raca
            }
            return render(request, template_name, context=context)
# Atualização feita pelo cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def cliente_pet_update(request, pk):
    template_name = 'pet/cliente_pet_update.html'
    obj = Pet.objects.get(id=pk)
    especie = Especie.objects.all().order_by('especie')
    raca = []

    if request.method == 'GET':
        form = PetClienteUpdateForm(instance=obj)
        context = {
            'form_pet': form,
            'obj': obj,
            'especie': especie,
            'raca': raca,
        }
        return render(request, template_name, context=context)
    if request.method == 'POST':
        form = PetClienteUpdateForm(request.POST, request.FILES, instance=obj)
       
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            form.save()
            return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={"pk": obj.pk}))
        else:
            context = { 
                'form_pet': form,
                'obj': obj,
                'especie': especie,
                'raca': raca
            }
            return render(request, template_name, context=context)
# Adicionar um novo tutor ao pet já existente

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

