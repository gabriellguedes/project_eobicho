from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from .forms import anamneseForm, formPet
from .models import PetModel, AnamneseModel

def anamnese(request):
    template = 'anamnese.html'
    if request.method == 'GET':
        form = anamneseForm()
        context = {
            'form':form
        }
        return render(request, template, context=context)
    else:
        form = anamneseForm(request.POST)
        if form.is_valid():
            pet = form.save()
            form = anamneseForm()
        
        context = {
            'form':form
        }
        
        return render(request, template, context=context)
    return render(request, template)

#Cadastro 
def form(request):
    template = 'pet/formpet_form.html'
    if request.method == 'GET':
        form = formPet()
        context = {
            'form':form
        }
        return render(request, template, context=context)
    else:
        form = formPet(request.POST)
        if form.is_valid():
            pet = form.save()
            form = formPet()
        
        context = {
            'form':form
        }
        
        return render(request, template, context=context)

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



#Atualização
def detailPet(request, pk):
    template ='pet/formpet_detail.html'
    obj = PetModel.objects.get(pk=pk)
    context = { 'object': obj }
    return render(request, template, context) 


#Atualização
class updatePet(UpdateView):
    template_name = 'pet/formpet_update.html'
    model = PetModel
    fields = '__all__'
    success_url = reverse_lazy('pet:list')

#Apagar    
class deletePet(DeleteView):
    queryset = PetModel.objects.all()
    success_url = reverse_lazy('pet:list')
    
