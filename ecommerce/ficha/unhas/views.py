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
  
#Unhas 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def unhas_add(request):
    template_name = 'unhas/unhas_add.html'
    if request.method == 'GET':
        form = UnhasForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = UnhasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:unhas:unhas_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar unhas cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def unhas_list(request):
    template_name='unhas/unhas_list.html'
    objeto = Unhas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar unhas cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def unhas_update(request, pk):
    template_name = 'unhas/unhas_update.html'
    objeto = Unhas.objects.get(id=pk)
    if request.method == 'GET':
        form = UnhasForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = UnhasForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:unhas:unhas_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma unhas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def unhas_delete(request, pk):
    template_name = 'unhas/unhas_delete.html'
    objeto = Unhas.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:unhas:unhas_list'))