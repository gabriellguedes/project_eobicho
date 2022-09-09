from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from datetime import datetime
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from ecommerce.ficha.models import Ficha
from ecommerce.ficha.forms import FichaForm
from .forms import PetForm
from .models import Pet

#Cadastro Pet e Ficha
def createPet(request):
    template = 'form_create.html'
    pet_form = Pet()
    a_form = inlineformset_factory(
        Pet,
        Ficha,
        form= FichaForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form= PetForm(request.POST, instance=pet_form, prefix='main')
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
        form= PetForm(instance=pet_form, prefix='main')
        formset= a_form(instance=pet_form, prefix='pet')
    context={
        'form': form,
        'formset': formset
    }    
    return render(request, template, context)   



#Lista de Exibição Paginação
def paginacao(request):
    template = 'pet/formpet_list.html'
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '5')
    
    if not (parametro_limit.isdigit() and int(parametro_limit)>0):
        parametro_limit = '10'

    pets = Pet.objects.get_queryset().order_by('id')
    pets_paginator = Paginator(pets, parametro_limit)

    objects = Pet.objects.all()
    
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

#Apagar    
class deletePet(DeleteView):
    queryset = Pet.objects.all()
    success_url = reverse_lazy('pet:list')

