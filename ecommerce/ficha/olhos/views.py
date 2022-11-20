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

#Olhos 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def olhos_add(request):
    template_name = 'olhos/olhos_add.html'
    if request.method == 'GET':
        form = OlhosForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = OlhosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:olhos:olhos_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar boca cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def olhos_list(request):
    template_name='olhos/olhos_list.html'
    objeto = Olhos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar boca cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def olhos_update(request, pk):
    template_name = 'olhos/olhos_update.html'
    objeto = Olhos.objects.get(id=pk)
    if request.method == 'GET':
        form = OlhosForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = OlhosForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:olhos:olhos_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma boca
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def olhos_delete(request, pk):
    template_name = 'olhos/olhos_delete.html'
    objeto = Olhos.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:olhos:olhos_list'))