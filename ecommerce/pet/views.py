from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from .models import formPet
from .forms import CadastroPet

def FormInspecaoPet(request):
	return render(request, 'formInspecao.html')

#Cadastro 
def form(request):
    if request.method == 'GET':
        form = CadastroPet()
        context = {
            'form':form
        }
        return render(request, 'pet/formpet_form.html', context=context)
    else:
        form = CadastroPet(request.POST)
        if form.is_valid():
            pet = form.save()
            form = CadastroPet()
        
        context = {
            'form':form
        }
        
        return render(request, 'pet/formpet_form.html', context=context)

#Lista de Exibição e Pesquisa
def paginacao(request):
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '5')
    
    if not (parametro_limit.isdigit() and int(parametro_limit)>0):
        parametro_limit = '10'

    pets = formPet.objects.all()
    pets_paginator = Paginator(pets, parametro_limit)

    search = request.GET.get('search')
    if search:
        pets = pets.filter(nome__icontains=search)

    try:
        page = pets_paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = pets_paginator.page(1)
       

    context = {
        'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'pets': page,
        'object_list':pets
    }
    return render(request, 'pet/formpet_list.html', context)

#Atualização
def detailPet(request, pk):
    template ='pet/formpet_detail.html'
    obj = formPet.objects.get(pk=pk)
    context = { 'object': obj }
    return render(request, template, context) 


#Atualização
class updatePet(UpdateView):
    template_name = 'pet/formpet_update.html'
    model = formPet
    fields = '__all__'
    success_url = reverse_lazy('pet:list')

#Apagar    
class deletePet(DeleteView):
    queryset = formPet.objects.all()
    success_url = reverse_lazy('pet:list')
    
