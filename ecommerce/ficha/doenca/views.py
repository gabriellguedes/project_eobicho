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

# Criar uma Doença
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def doenca_add(request):
    template_name = 'doenca/doenca_add.html'
    if request.method == 'GET':
        form = DoencaForm()
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = DoencaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:doenca:doenca_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# Listar todas as doenças
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def doenca_list(request):
    template_name = 'doenca/doenca_list.html'
    objeto = Doenca.objects.all()
    context = {'form': objeto}
    return render(request, template_name, context=context)
# Atualizar doença
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def doenca_update(request, pk):
    template_name = 'doenca/doenca_update.html'
    objeto = Doenca.objects.get(id=pk)
    if request.method == 'GET':
        form = DoencaForm(instance=objeto)
        context = { 'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = DoencaForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:doenca:doenca_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# Deletar doença
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def doenca_delete(request, pk):
    template_name ='doenca/doenca_delete.html'
    objeto = Doenca.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:doenca:doenca_list'))