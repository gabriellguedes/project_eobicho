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

#Orelhas 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def orelhas_add(request):
    template_name = 'orelhas/orelhas_add.html'
    if request.method == 'GET':
        form = OrelhasForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = OrelhasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:orelhas:orelhas_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar orelhas cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def orelhas_list(request):
    template_name='orelhas/orelhas_list.html'
    objeto = Orelhas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar orelhas cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def orelhas_update(request, pk):
    template_name = 'orelhas/orelhas_update.html'
    objeto = Orelhas.objects.get(id=pk)
    if request.method == 'GET':
        form = OrelhasForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = OrelhasForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:orelhas:orelhas_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma orelhas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def orelhas_delete(request, pk):
    objeto = Orelhas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:orelhas:orelhas_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)