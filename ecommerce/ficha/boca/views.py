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

#Boca
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def boca_add(request):
    template_name = 'boca/boca_add.html'
    if request.method == 'GET':
        form = BocaForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = BocaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:boca:boca_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar boca cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def boca_list(request):
    template_name='boca/boca_list.html'
    objeto = Boca.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar boca cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def boca_update(request, pk):
    template_name = 'boca/boca_update.html'
    objeto = Boca.objects.get(id=pk)
    if request.method == 'GET':
        form = BocaForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = BocaForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:boca:boca_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma boca
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def boca_delete(request, pk):
    template_name = 'boca/boca_delete.html'
    objeto = Boca.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:boca:boca_list'))