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

# Adicionar Novo Tipo de Pelos
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def pelos_add(request):
    template_name = 'pelos/pelos_add.html'
    if request.method == 'GET':
        form = PelosForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = PelosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:pelos_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar Tipos de pelos cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def pelos_list(request):
    template_name='pelos/pelos_list.html'
    objeto = Pelos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar Tipo de pelo cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def pelos_update(request, pk):
    template_name = 'pelos/pelos_update.html'
    objeto = Pelos.objects.get(id=pk)
    if request.method == 'GET':
        form = PelosForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = PelosForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:pelos_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar um Tipo de Pelo
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def pelos_delete(request, pk):
    template_name = 'pelos/pelos_delete.html'
    objeto = Pelos.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:pelos:pelos_list'))
   
# Adicionar Novo condição de Pelos
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def estado_pelos_add(request):
    template_name = 'pelos/estado_pelos_add.html'
    if request.method == 'GET':
        form = Estado_pelosForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = Estado_pelosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:estado_pelos_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar condição dos pelos cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def estado_pelos_list(request):
    template_name='pelos/estado_pelos_list.html'
    objeto = Estado_pelos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar condição do pelo cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def estado_pelos_update(request, pk):
    template_name = 'pelos/estado_pelos_update.html'
    objeto = Estado_pelos.objects.get(id=pk)
    if request.method == 'GET':
        form = Estado_pelosForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = Estado_pelosForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:estado_pelos_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar um Condição de Pelo
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def estado_pelos_delete(request, pk):
    template_name = 'pelos/estado_pelos_delete.html'
    objeto = Estado_pelos.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:pelos:estado_pelos_list'))
   
# Adicionar Novo Tipo de Pelos
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def condicao_pelos_add(request):
    template_name = 'pelos/condicao_pelos_add.html'
    if request.method == 'GET':
        form = Condicao_pelosForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = Condicao_pelosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:condicao_pelos_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar Tipos de pelos cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def condicao_pelos_list(request):
    template_name='pelos/condicao_pelos_list.html'
    objeto = Condicao_pelos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar Tipo de pelo cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def condicao_pelos_update(request, pk):
    template_name = 'pelos/condicao_pelos_update.html'
    objeto = Condicao_pelos.objects.get(id=pk)
    if request.method == 'GET':
        form = Condicao_pelosForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = Condicao_pelosForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:condicao_pelos_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar um Tipo de Pelo
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def condicao_pelos_delete(request, pk):
    template_name = 'pelos/condicao_pelos_delete.html'
    objeto = Condicao_pelos.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:pelos:condicao_pelos_list'))

# PELAGEM - CRIAR UM NOVO TIPO DE PELAGEM
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def pelagem_add(request):
    template_name = 'pelagem/pelagem_add.html'
    if request.method == 'GET':
        form = PelagemForm()
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = PelagemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:pelagem_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# ATUALIZAR/ALTERAR UM TIPODE PELAGEM
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def pelagem_update(request, pk):
    template_name = 'pelagem/pelagem_update.html'
    obj = Pelagem.objects.get(id=pk)
    if request.method == 'GET':
        form = PelagemForm(instance=obj)
        context = {'form':form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = PelagemForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:pelagem_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# LISTAR TODOS OS TIPOS DE PELAGEM CADASTRADOS
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def pelagem_list(request):
    template_name = 'pelagem/pelagem_list.html'
    obj = Pelagem.objects.all()
    context = {'form': obj}
    return render(request, template_name, context=context)
# DELETAR/APAGAR UM TIPO DE PELAGEM
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def pelagem_delete(request, pk):
    template_name = 'pelagem/pelagem_delete.html'
    objeto = Pelagem.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:pelos:pelagem_list'))

# COLORAÇÃO - ADICIONAR UMA NOVA COLORAÇÃO DOS PELOS
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def coloracao_add(request):
    template_name = 'coloracao/coloracao_add.html'
    if request.method == 'GET':
        form = ColoracaoForm()
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = ColoracaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:coloracao_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# ATUALIZAR/ALTERAR UMA COLORAÇÃO CADASTRADA
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def coloracao_update(request, pk):
    template_name = 'coloracao/coloracao_update.html'
    obj = Coloracao.objects.get(id=pk)
    if request.method == 'GET':
        form = ColoracaoForm(instance=obj)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = ColoracaoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos:coloracao_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# LISTAR TODAS AS COLORAÇÕES CADASTRADAS    
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def coloracao_list(request):
    template_name = 'coloracao/coloracao_list.html'
    obj = Coloracao.objects.all()
    context = {'form': obj}
    return render(request, template_name, context=context)
# DELETAR/APAGAR UMA COLORAÇÃO CADASTRADA
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def coloracao_delete(request, pk):
    template_name = 'coloracao/coloracao_delete.html'
    objeto = Coloracao.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:pelos:coloracao_list'))
