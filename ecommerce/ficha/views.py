from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ecommerce.pet.models import Pet
from .models import Ficha
from .forms import FichaForm
from ecommerce.pet.forms import PetForm
from django.forms import inlineformset_factory

# Criar uma nova ficha
def createFicha(request, pk):
    template_name = 'ficha_add.html'
    obj = Pet.objects.get(pk=pk)
    
    if request.method == 'GET':
        form = PetForm()
        form_ficha_factory = inlineformset_factory(Pet, Ficha, form=FichaForm, extra=1)
        form_ficha = form_ficha_factory()

        context = {
            'form':form_ficha,
            'pet': obj, 
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = PetForm(request.POST)
        form_ficha_factory = inlineformset_factory(Pet, Ficha, form=FichaForm)
        form_ficha = form_ficha_factory(request.POST)

        if form_ficha.is_valid():
            form_ficha.instance = obj    
            form_ficha.save()
            return HttpResponseRedirect(reverse('pet:pet_list'))
        else:
            context = {
                'form':form_ficha
            }

            return render(request, template_name, context=context)


#Listar todas as fichas cadastradas
def listFicha(request):
    template_name = 'ficha_list.html'
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '5')
    
    if not (parametro_limit.isdigit() and int(parametro_limit)>0):
        parametro_limit = '10'

    fichas = Ficha.objects.get_queryset().order_by('id')
    fichas_paginator = Paginator(fichas, parametro_limit)

    lista = Ficha.objects.all()
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

#Visualizar ficha antiga
def detailFicha(request, pk, n):
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
