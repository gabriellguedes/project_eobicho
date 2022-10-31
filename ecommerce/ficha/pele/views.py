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

# Adicionar Novo Tipo de Pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pele_add(request):
    template_name = 'pele/pele_add.html'
    if request.method == 'GET':
        form = PeleForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = PeleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pele:pele_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar Tipos de peles cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pele_list(request):
    template_name='pele/pele_list.html'
    objeto = Pele.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar Tipo de pele cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pele_update(request, pk):
    template_name = 'pele/pele_update.html'
    objeto = Pele.objects.get(id=pk)
    if request.method == 'GET':
        form = PeleForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = PeleForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pele:pele_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar um Tipo de Pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pele_delete(request, pk):
    objeto = Pele.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
    else:
        msg = 'Item não encotrado'
    return HttpResponseRedirect(reverse('fichas:pele:pele_list'))

# Adicionar Ectoparasitas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def ectoparasitas_add(request):
    template_name='pele/ectoparasitas_add.html'
    if request.method == 'GET':
        form = EctoparasitasForm()
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = EctoparasitasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pele:ectoparasitas_list'))
        else:
            context = { 'form': form}
            return render(request, template_name, context=context)
# Listar ectoparasitas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def ectoparasitas_list(request):
    template_name = 'pele/ectoparasitas_list.html'
    objeto = Ectoparasitas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Update ectoparasitas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def ectoparasitas_update(request, pk):
    template_name='pele/ectoparasitas_update.html'
    objeto = Ectoparasitas.objects.get(id=pk)
    if request.method == 'GET':
        form = EctoparasitasForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = EctoparasitasForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pele:ectoparasitas_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# Deletar ectoparasitas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def ectoparasitas_delete(request, pk):
    objeto = Ectoparasitas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:pele:ectoparasitas_list'))
    else:
        context = {'form':form}
        return render(request, context=context)

# Add infec_pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def infec_pele_add(request):
    template_name = 'pele/infec_pele_add.html'
    if request.method == 'GET':
        form = Infec_peleForm()
        context = {'form':form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = Infec_peleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pele:infec_pele_list'))
        else: 
            context = {'form': form}
            return render(request, template_name, context=context)
# Listar infec_pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def infec_pele_list(request):
    template_name = 'pele/infec_pele_list.html'
    objeto = Infec_pele.objects.all()
    context = {'form': objeto}
    return render(request, template_name, context=context)
# Atualizar infec_pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def infec_pele_update(request, pk):
    template_name = 'pele/infec_pele_update.html'
    objeto = Infec_pele.objects.get(id=pk)
    if request.method == 'GET':
        form = Infec_peleForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = Infec_peleForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pele:infec_pele_list'))
        else:
            context = {'form': form}
            return render(request,template_name, context=context)
# Deletar infec_pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def infec_pele_delete(request, pk):
    objeto = Infec_pele.objects.get(id=pk)
    if objeto != '':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:pele:infec_pele_list'))
    else:
        msg = 'Item não existe!'
        context = {'msg': msg }
        return render(request, context=context)    