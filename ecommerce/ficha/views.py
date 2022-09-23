from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ecommerce.pet.models import Pet
from .models import Ficha, Prontuario, Pele, Doenca
from .forms import FichaForm, ProntuarioForm, PeleForm, DoencaForm
from ecommerce.pet.forms import PetForm
from django.forms import inlineformset_factory

# Criar uma nova ficha
def prontuario_create(request, pk):
    template_name = 'add_test.html'
    obj = Pet.objects.get(pk=pk)
    
    if request.method == 'GET':
        form = PetForm()
        form_ficha_factory = inlineformset_factory(Pet, Ficha, form=FichaForm, extra=1)
        form_ficha = form_ficha_factory()

        context = {
            'form':form_ficha,
            'pet': obj, 
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = PetForm(request.POST)
        form_ficha_factory = inlineformset_factory(Pet, Ficha, form=FichaForm)
        form_ficha = form_ficha_factory(request.POST)

        if form_ficha.is_valid():
            form_ficha.instance = obj    
            form_ficha.save()
            return HttpResponseRedirect(reverse('pet:pet_list'))
        else:
            context = {
                'form':form_ficha
            }

            return render(request, template_name, context=context)
# Listar todas as fichas cadastradas
def prontuario_list(request):
    template_name = 'ficha_list.html'
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '5')
    
    if not (parametro_limit.isdigit() and int(parametro_limit)>0):
        parametro_limit = '10'

    fichas = Ficha.objects.get_queryset().order_by('id')
    fichas_paginator = Paginator(fichas, parametro_limit)

    lista = Ficha.objects.all()
    pet = Pet.objects.all()

    try:
        page = fichas_paginator.page(parametro_page)

    except (EmptyPage, PageNotAnInteger):
        page = fichas_paginator.page(1)

    context = { 
        'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'fichas': page,
        'lista': lista,
        'pet': pet,
        }
    return render(request, template_name, context=context)
# Visualizar ficha antiga
def prontuario_detail(request, pk, n):
    template_name = 'ficha_detail.html'
    pet = Pet.objects.get(pk=pk)
    ficha = pet.fichaPets.get(id=n)
    last_fichas = pet.fichaPets.all()
    context={ 
        'pet': pet,
        'ficha': ficha,
        'last_fichas': last_fichas
     }
    return render(request, template_name, context)

# Adicionar Novo Tipo de Pele
def pele_add(request):
    template_name = 'itens_ficha/pele/pele_add.html'
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
            return HttpResponseRedirect(reverse('fichas:pele_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar Tipos de peles cadastradas
def pele_list(request):
    template_name='itens_ficha/pele/pele_list.html'
    objeto = Pele.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar Tipo de pele cadastrada
def pele_update(request, pk):
    template_name = 'itens_ficha/pele/pele_update.html'
    objeto = Pele.objects.get(id=pk)
    if request.method == 'GET':
        form = PeleForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = PeleForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pele_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar um Tipo de Pele
def pele_delete(request, pk):
    objeto = Pele.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
    else:
        msg = 'Item não encotrado'
   

# Criar uma Doença
def doenca_add(request):
    template_name = 'itens_ficha/doenca/doenca_add.html'
    if request.method == 'GET':
        form = DoencaForm()
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = DoencaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:doenca_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# Listar todas as doenças
def doenca_list(request):
    template_name = 'itens_ficha/doenca/doenca_list.html'
    objeto = Doenca.objects.all()
    context = {'form': objeto}
    return render(request, template_name, context=context)
# Atualizar doença
def doenca_update(request, pk):
    template_name = 'itens_ficha/doenca/doenca_update.html'
    objeto = Doenca.objects.get(id=pk)
    if request.method == 'GET':
        form = DoencaForm(instance=objeto)
        context = { 'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = DoencaForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:doenca_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# Deletar doença
def doenca_delete(request, pk):
    objeto = Doenca.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:doenca_list'))
    else: 
        msg = 'Item não existe!' 
        context = {'msg': msg}
        return render(request, context=context)


