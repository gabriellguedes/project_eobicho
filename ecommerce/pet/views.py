from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from datetime import datetime
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from .forms import anamneseForm, formPet
from .models import PetModel, AnamneseModel

#Cadastro Pet e Ficha
def createPet(request):
    template = 'form_create.html'
    pet_form = PetModel()
    a_form = inlineformset_factory(
        PetModel,
        AnamneseModel,
        form=anamneseForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form= formPet(request.POST, instance=pet_form, prefix='main')
        formset= a_form(
            request.POST,
            instance=pet_form, 
            prefix='pet',
        )
        if form.is_valid() and formset.is_valid():
            form=form.save()
            formset=formset.save()
            url = 'pet:detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form= formPet(instance=pet_form, prefix='main')
        formset= a_form(instance=pet_form, prefix='pet')
    context={
        'form': form,
        'formset': formset
    }    
    return render(request, template, context)   

def createFicha(request):
    template = 'anamnese.html'
    cad = PetModel.objects.all()
    pet = PetModel()
    if request.method == 'POST':
        form = anamneseForm(request.POST)
        if form.is_valid():
            form =form.save()
            url = 'pet:detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form= anamneseForm(instance=pet, prefix='main')
    context = {
        'form': form,
        'cad': cad
    }        
    return render(request, template, context)
#Lista de Exibição e Pesquisa
def paginacao(request):
    template = 'pet/formpet_list.html'
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '5')
    
    if not (parametro_limit.isdigit() and int(parametro_limit)>0):
        parametro_limit = '10'

    pets = PetModel.objects.get_queryset().order_by('id')
    pets_paginator = Paginator(pets, parametro_limit)

    objects = PetModel.objects.all()
    
    search = request.GET.get('search')
    if search:
        objects = objects.filter(nome__icontains=search)
        return render(request, template)
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
    return render(request, template, context)

def listFicha(request):
    template_name = 'ficha_list.html'
    lista = AnamneseModel.objects.all()
    context = { 'lista': lista}
    return render(request, template_name, context)

#Vizualizar Pet e Ficha
def detailPet(request, pk):
    template ='pet/formpet_detail.html'
    
    obj = PetModel.objects.get(pk=pk)
    ficha = obj.fichaPets.last()
    last_fichas = obj.fichaPets.all()
    context = { 
    'object': obj,
    'ficha': ficha,
    'last_fichas': last_fichas,
     }
    return render(request, template, context) 
#Visualizar ficha antiga
def detailFicha(request, pk):
    template_name = 'ficha_detail.html'
    ficha = AnamneseModel.objects.get(pk=pk)
    context={ 'ficha': ficha }
    return render(request, template_name, context)


#Atualização
class updatePet(UpdateView):
    template_name = 'pet/formpet_update.html'
    model = PetModel
    fields = '__all__'
    success_url = reverse_lazy('pet:list')
"""
class updateFicha(UpdateView):
    template_name = 'anamnese.html'
    model = AnamneseModel
    fields = '__all__'
    success_url = reverse_lazy('pet:list')"""

#Apagar    
class deletePet(DeleteView):
    queryset = PetModel.objects.all()
    success_url = reverse_lazy('pet:list')
    
