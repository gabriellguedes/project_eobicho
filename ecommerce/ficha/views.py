from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ecommerce.pet.models import Pet
from .models import *
from .forms import *
from ecommerce.pet.forms import PetForm
from django.forms import inlineformset_factory

# Criar uma nova ficha
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def prontuario_create(request, pk):
    template_name = 'ficha_add.html'
    obj = Pet.objects.get(pk=pk)
    
    if request.method == 'GET':
        form = PetForm()
        
        form_ficha_factory = inlineformset_factory(Pet, Anamnese, form=AnamneseForm, extra=1)
        form_ficha = form_ficha_factory()

        context = {
            'form':form_ficha,
            'pet': obj, 
        }
        return render(request, template_name, context=context)
    
    elif request.method == 'POST':
        
        form = PetForm(request.POST)
        form_ficha_factory = inlineformset_factory(Pet, Anamnese, form=AnamneseForm)
        form_ficha = form_ficha_factory(request.POST)

        if form_ficha.is_valid():
            user = form_ficha.save(commit=False)
            form_ficha.instance = obj
            user[0].funcionario = request.user    
            form_ficha.save()
            return HttpResponseRedirect(reverse('services:new_ficha', kwargs={"pk": obj.pk}))
        else:
            context = {
                'form':form_ficha,
                'pet': obj,
            }
            context['msg'] = 'Erro! Avalição não foi salva.'
            context['class'] = 'alert alert-danger'
            return render(request, template_name, context=context)
# Listar todas as fichas cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def prontuario_list(request):
    template_name = 'ficha_list.html'
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '5')
    
    if not (parametro_limit.isdigit() and int(parametro_limit)>0):
        parametro_limit = '10'

    fichas = Anamnese.objects.get_queryset().order_by('id')
    fichas_paginator = Paginator(fichas, parametro_limit)

    lista = Anamnese.objects.all()
    pet = Pet.objects.all()

    try:
        page = fichas_paginator.page(parametro_page)

    except (EmptyPage, PageNotAnInteger):
        page = fichas_paginator.page(1)

    context = { 
        'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'fichas': page,
        'lista': lista,
        'pet': pet,
        }
    return render(request, template_name, context=context)
# Visualizar ficha antiga
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def prontuario_detail(request, pk, n):
    template_name = 'ficha_detail.html'
    pet = Pet.objects.get(pk=pk)
    ficha = pet.fichaPets.get(id=n)
    last_fichas = pet.fichaPets.all()
    context={ 
        'pet': pet,
        'ficha': ficha,
        'last_fichas': last_fichas
     }
    return render(request, template_name, context)

def add_test(request):
    template_name = 'add_test.html'
    if request.method == 'GET':
        form = TestForm()
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:ficha_list'))
        else:
            context = {'form':form}
            return render(request, template_name, context=context)




