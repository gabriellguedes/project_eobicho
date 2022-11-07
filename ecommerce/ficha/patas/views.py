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

#Patas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def patas_add(request):
    template_name = 'patas/patas_add.html'
    if request.method == 'GET':
        form = PatasForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = PatasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:patas:patas_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar patas cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def patas_list(request):
    template_name='patas/patas_list.html'
    objeto = Patas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar patas cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def patas_update(request, pk):
    template_name = 'patas/patas_update.html'
    objeto = Patas.objects.get(id=pk)
    if request.method == 'GET':
        form = PatasForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = PatasForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:patas:patas_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma patas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def patas_delete(request, pk):
    template_name = 'patas/patas_delete.html'
    objeto = Patas.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:patas:patas_list'))