from django.shortcuts import render, resolve_url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from ecommerce.ficha.models import Ficha
from ecommerce.ficha.forms import FichaForm
from .forms import PetForm
from .models import Pet, Especie, Raca

#Cadastro Pet
def pet_add(request):
    template_name = 'pet/formpet_form.html'
    form = PetForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pet:list'))
    context = {'form': form}
    return render(request, template_name, context)

#Lista de Exibição Paginação
def paginacao(request):
    template_name = 'pet/formpet_list.html'
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
def detailPet(request, pk):
    template ='pet/formpet_detail.html'
    obj = Pet.objects.get(id=pk)
    ficha = obj.fichaPets.last()
    last_fichas = obj.fichaPets.all()
    context = { 
        'pet': obj,
        'ficha': ficha,
        'last_fichas': last_fichas,
     }
    return render(request, template, context) 

#Atualização
class updatePet(UpdateView):
    template_name = 'pet/formpet_update.html'
    model = Pet
    fields = '__all__'
    success_url = reverse_lazy('pet:list')

#Visualizar raças
def raca_view(request):
    template_name= 'formpet_form.html'
    raca = Raca.objects.filter(especie=1)
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)