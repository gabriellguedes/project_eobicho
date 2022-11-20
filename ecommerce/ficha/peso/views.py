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
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

#Adicionar peso ao pet 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission') 
def peso_add(request, pk):
    template_name='peso/peso_add.html'
    
    obj = Pet.objects.get(pk=pk)

     # Add Peso
    if request.method == 'GET':
        form = PetForm()

        form_peso_factory = inlineformset_factory(Pet, Peso, form=PesoForm, extra=1, can_delete=False)
        form_peso = form_peso_factory()

        context={
            'pet': obj,
            'form': form_peso,
        }
        return render(request, template_name, context=context)
        
    elif request.method == 'POST':
        form = PetForm(request.POST)
        form_peso_factory = inlineformset_factory(Pet, Peso, form=PesoForm, can_delete=False)
        form_peso = form_peso_factory(request.POST)
        
        if form_peso.is_valid():
            form = form_peso.save(commit=False)
            form[0].user = request.user
            form_peso.instance = obj
            form_peso.save()
            return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={"pk": obj.pk}))
        else:
            context = {
                'form': form_peso,
                'pet': obj,
            }
            return render(request, template_name, context=context)
# Alterar Peso do Pet            
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission') 
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def peso_update(request, pk):
    template_name = 'peso/peso_update.html'
    obj = Peso.objects.get(id=pk)
    pet = obj.pet

    if request.method == 'GET':
        form = PesoUpdateForm(instance=obj)
        context = { 'form': form, 'pet': pet }
        return render(request, template_name, context=context)
    
    elif request.method == 'POST':
        form = PesoUpdateForm(request.POST, instance=obj) 

        if form.is_valid():
            
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={'pk': obj.pet.id }))
        else:
            context = { 'form': form, 'pet': pet }
            return render(request, template_name, context=context)

#pesar o pet

@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def peso_add_for_banho(request, pk):
    template_name = 'peso/add_peso_bt.html'
    obj = Pet.objects.get(pk=pk)
     # Add Peso
    if request.method == 'GET':
        form = PetForm()

        form_peso_factory = inlineformset_factory(Pet, Peso, form=PesoForm, extra=1, can_delete=False)
        form_peso = form_peso_factory()

        context={
            'pet': obj,
            'form': form_peso,
        }
        return render(request, template_name, context=context)
        
    elif request.method == 'POST':
        form = PetForm(request.POST)
        form_peso_factory = inlineformset_factory(Pet, Peso, form=PesoForm, can_delete=False)
        form_peso = form_peso_factory(request.POST)
        
        if form_peso.is_valid():
            form = form_peso.save(commit=False)
            form[0].user = request.user
            form_peso.instance = obj
            form_peso.save()
            return HttpResponseRedirect(reverse('services:new_ficha', kwargs={"pk": obj.pk}))
        else:
            context = {
                'form': form_peso,
                'pet': obj,
            }
            return render(request, template_name, context=context)