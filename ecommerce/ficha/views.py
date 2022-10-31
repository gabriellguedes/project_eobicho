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

################################################################################
# Criar uma nova ficha
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def prontuario_create(request, pk):
    template_name = 'ficha_add.html'
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
            user = form_ficha.save(commit=False)
            form_ficha.instance = obj
            user[0].funcionario = request.user    
            form_ficha.save()
            return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={"pk": obj.pk}))
        else:
            context = {
                'form':form_ficha
            }

            return render(request, template_name, context=context)
# Listar todas as fichas cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
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
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
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

#################################################################################
# Adicionar Novo Tipo de Pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
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
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pele_list(request):
    template_name='itens_ficha/pele/pele_list.html'
    objeto = Pele.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar Tipo de pele cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
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
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pele_delete(request, pk):
    objeto = Pele.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
    else:
        msg = 'Item não encotrado'

#################################################################################
# Criar uma Doença
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
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
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def doenca_list(request):
    template_name = 'itens_ficha/doenca/doenca_list.html'
    objeto = Doenca.objects.all()
    context = {'form': objeto}
    return render(request, template_name, context=context)
# Atualizar doença
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
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
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def doenca_delete(request, pk):
    objeto = Doenca.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:doenca_list'))
    else: 
        msg = 'Item não existe!' 
        context = {'msg': msg}
        return render(request, context=context)

#################################################################################
# Adicionar Ectoparasitas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def ectoparasitas_add(request):
    template_name='itens_ficha/pele/ectoparasitas_add.html'
    if request.method == 'GET':
        form = EctoparasitasForm()
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = EctoparasitasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:ectoparasitas_list'))
        else:
            context = { 'form': form}
            return render(request, template_name, context=context)
# Listar ectoparasitas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def ectoparasitas_list(request):
    template_name = 'itens_ficha/pele/ectoparasitas_list.html'
    objeto = Ectoparasitas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Update ectoparasitas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def ectoparasitas_update(request, pk):
    template_name='itens_ficha/pele/ectoparasitas_update.html'
    objeto = Ectoparasitas.objects.get(id=pk)
    if request.method == 'GET':
        form = EctoparasitasForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = EctoparasitasForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:ectoparasitas_list'))
        else:
            context = {'form': form}
            return render(request, template_name, context=context)
# Deletar ectoparasitas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def ectoparasitas_delete(request, pk):
    objeto = Ectoparasitas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:ectoparasitas_list'))
    else:
        context = {'form':form}
        return render(request, context=context)

#################################################################################
# Add infec_pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def infec_pele_add(request):
    template_name = 'itens_ficha/pele/infec_pele_add.html'
    if request.method == 'GET':
        form = Infec_peleForm()
        context = {'form':form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = Infec_peleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:infec_pele_list'))
        else: 
            context = {'form': form}
            return render(request, template_name, context=context)
# Listar infec_pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def infec_pele_list(request):
    template_name = 'itens_ficha/pele/infec_pele_list.html'
    objeto = Infec_pele.objects.all()
    context = {'form': objeto}
    return render(request, template_name, context=context)
# Atualizar infec_pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def infec_pele_update(request, pk):
    template_name = 'itens_ficha/pele/infec_pele_update.html'
    objeto = Infec_pele.objects.get(id=pk)
    if request.method == 'GET':
        form = Infec_peleForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = Infec_peleForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:infec_pele_list'))
        else:
            context = {'form': form}
            return render(request,template_name, context=context)
# Deletar infec_pele
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def infec_pele_delete(request, pk):
    objeto = Infec_pele.objects.get(id=pk)
    if objeto != '':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:infec_pele_list'))
    else:
        msg = 'Item não existe!'
        context = {'msg': msg }
        return render(request, context=context)    

#################################################################################
# Adicionar Novo Tipo de Pelos
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pelos_add(request):
    template_name = 'itens_ficha/pelos/pelos_add.html'
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
            return HttpResponseRedirect(reverse('fichas:pelos_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar Tipos de pelos cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pelos_list(request):
    template_name='itens_ficha/pelos/pelos_list.html'
    objeto = Pelos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar Tipo de pelo cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pelos_update(request, pk):
    template_name = 'itens_ficha/pelos/pelos_update.html'
    objeto = Pelos.objects.get(id=pk)
    if request.method == 'GET':
        form = PelosForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = PelosForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:pelos_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar um Tipo de Pelo
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def pelos_delete(request, pk):
    objeto = Pelos.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:pelos_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)
   
#################################################################################
# Adicionar Novo condição de Pelos
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def estado_pelos_add(request):
    template_name = 'itens_ficha/pelos/estado_pelos_add.html'
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
            return HttpResponseRedirect(reverse('fichas:estado_pelos_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar condição dos pelos cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def estado_pelos_list(request):
    template_name='itens_ficha/pelos/estado_pelos_list.html'
    objeto = Estado_pelos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar condição do pelo cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def estado_pelos_update(request, pk):
    template_name = 'itens_ficha/pelos/estado_pelos_update.html'
    objeto = Estado_pelos.objects.get(id=pk)
    if request.method == 'GET':
        form = Estado_pelosForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = Estado_pelosForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:estado_pelos_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar um Condição de Pelo
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def estado_pelos_delete(request, pk):
    objeto = Estado_pelos.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:estado_pelos_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)
   
#################################################################################
# Adicionar Novo Tipo de Pelos
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def condicao_pelos_add(request):
    template_name = 'itens_ficha/pelos/condicao_pelos_add.html'
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
            return HttpResponseRedirect(reverse('fichas:condicao_pelos_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar Tipos de pelos cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def condicao_pelos_list(request):
    template_name='itens_ficha/pelos/condicao_pelos_list.html'
    objeto = Condicao_pelos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar Tipo de pelo cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def condicao_pelos_update(request, pk):
    template_name = 'itens_ficha/pelos/condicao_pelos_update.html'
    objeto = Condicao_pelos.objects.get(id=pk)
    if request.method == 'GET':
        form = Condicao_pelosForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = Condicao_pelosForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:condicao_pelos_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar um Tipo de Pelo
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def condicao_pelos_delete(request, pk):
    objeto = Condicao_pelos.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:condicao_pelos_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)
   
#################################################################################
#Boca
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def boca_add(request):
    template_name = 'itens_ficha/boca/boca_add.html'
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
            return HttpResponseRedirect(reverse('fichas:boca_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar boca cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def boca_list(request):
    template_name='itens_ficha/boca/boca_list.html'
    objeto = Boca.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar boca cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def boca_update(request, pk):
    template_name = 'itens_ficha/boca/boca_update.html'
    objeto = Boca.objects.get(id=pk)
    if request.method == 'GET':
        form = BocaForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = BocaForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:boca_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma boca
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def boca_delete(request, pk):
    objeto = Boca.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:boca_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)

#################################################################################   
#Unhas 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def unhas_add(request):
    template_name = 'itens_ficha/unhas/unhas_add.html'
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
            return HttpResponseRedirect(reverse('fichas:unhas_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar unhas cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def unhas_list(request):
    template_name='itens_ficha/unhas/unhas_list.html'
    objeto = Unhas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar unhas cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def unhas_update(request, pk):
    template_name = 'itens_ficha/unhas/unhas_update.html'
    objeto = Unhas.objects.get(id=pk)
    if request.method == 'GET':
        form = UnhasForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = UnhasForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:unhas_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma unhas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def unhas_delete(request, pk):
    objeto = Unhas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:unhas_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)

#################################################################################
#Olhos 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def olhos_add(request):
    template_name = 'itens_ficha/olhos/olhos_add.html'
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
            return HttpResponseRedirect(reverse('fichas:olhos_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar boca cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def olhos_list(request):
    template_name='itens_ficha/olhos/olhos_list.html'
    objeto = Olhos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar boca cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def olhos_update(request, pk):
    template_name = 'itens_ficha/olhos/olhos_update.html'
    objeto = Olhos.objects.get(id=pk)
    if request.method == 'GET':
        form = OlhosForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = OlhosForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:olhos_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma boca
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def olhos_delete(request, pk):
    objeto = Olhos.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:olhos_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)

#################################################################################
#Orelhas 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def orelhas_add(request):
    template_name = 'itens_ficha/orelhas/orelhas_add.html'
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
            return HttpResponseRedirect(reverse('fichas:orelhas_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar orelhas cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def orelhas_list(request):
    template_name='itens_ficha/orelhas/orelhas_list.html'
    objeto = Orelhas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar orelhas cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def orelhas_update(request, pk):
    template_name = 'itens_ficha/orelhas/orelhas_update.html'
    objeto = Orelhas.objects.get(id=pk)
    if request.method == 'GET':
        form = OrelhasForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = OrelhasForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:orelhas_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma orelhas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def orelhas_delete(request, pk):
    objeto = Orelhas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:orelhas_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)

#################################################################################
#Patas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def patas_add(request):
    template_name = 'itens_ficha/patas/patas_add.html'
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
            return HttpResponseRedirect(reverse('fichas:patas_list'))
        else:
            context = {
                'form': form
            }    
            return render(request, template_name, context=context)
# Listar patas cadastradas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def patas_list(request):
    template_name='itens_ficha/patas/patas_list.html'
    objeto = Patas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar patas cadastrada
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def patas_update(request, pk):
    template_name = 'itens_ficha/patas/patas_update.html'
    objeto = Patas.objects.get(id=pk)
    if request.method == 'GET':
        form = PatasForm(instance=objeto)
        context = {'form': form}
        return render(request, template_name, context=context)
    elif request.method =='POST':
        form = PatasForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:patas_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)    
# Apagar uma patas
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def patas_delete(request, pk):
    objeto = Patas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:patas_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)

#################################################################################
#Adicionar peso ao pet 
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission') 
def peso_add(request, pk):
    template_name='itens_ficha/peso/peso_add.html'
    
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
def peso_update(request, pk):
    template_name = 'itens_ficha/peso/peso_update.html'
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

#################################################################################
# Add Espécie/Raça
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission') 
def especie_add(request):
    template_name = 'cad_pet/especie_add.html'
    
    if request.method == 'GET':
        form = EspecieForm()
        form_raca_factory = inlineformset_factory(Especie, Raca, form=RacaForm, extra=1, can_delete=False)
        form_raca = form_raca_factory()

        context = {
            'form': form,
            'form_raca': form_raca,
        }
        return render(request, template_name, context=context)

    elif request.method == 'POST':
        form = EspecieForm(request.POST)
        form_raca_factory = inlineformset_factory(Especie, Raca, form=RacaForm, extra=1)
        form_raca = form_raca_factory(request.POST)
        
        if form.is_valid() and form_raca.is_valid():
            especie = form.save()
            form_raca.instance = especie
            form_raca.save()
            return HttpResponseRedirect(reverse('fichas:especie_list'))
        else:
            context = {
             'form': form,
             'form_raca': form_raca
            }
            return render(request, template_name, context=context)
# Adicionar uma nova Especie
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def add_Especie(request):
    template_name = 'cad_pet/especie_add.html'
    form = EspecieForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(reverse('fichas:especie_list'))
    context ={'form': form}      
    return render(request, template_name, context=context)
# Listar as Especies
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def list_Especie(request):
    template_name = 'cad_pet/especie_list.html'
    obj = Especie.objects.all()
    context = { 'especie': obj }
    return render(request, template_name, context=context)
# Deletar uma Especie
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def delete_Especie(request, pk):
    obj = Especie.objects.get(id=pk)
    obj.delete()
    
    return HttpResponseRedirect(reverse('fichas:especie_list'))
# Atualizar/Alterar Espécies
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def update_Especie(request, pk):
    template_name = 'cad_pet/especie_update.html'
    obj_especie = Especie.objects.get(id=pk)
    if request.method == 'GET':
        form = EspecieForm(instance=obj_especie)
        context = { 'form': form }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = EspecieForm(request.POST, instance=obj_especie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:especie_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)

#################################################################################
# Adicionar Raça
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def add_Raca(request):
    template_name = 'cad_pet/raca_add.html'
    if request.method == 'GET':

        form = RacaForm()
        caracteristicas_factory_form = inlineformset_factory(Raca, Caracteristicas_Raca, form=Caracteristicas_RacaForm, extra=1, can_delete=False )
        caracteristicas_form = caracteristicas_factory_form()
        context = { 
            'raca': form,
            'caracteristicas': caracteristicas_form,
        }
        return render(request, template_name, context=context)
    if request.method=='POST':        
        form = RacaForm(request.POST)
        caracteristicas_factory_form = inlineformset_factory(Raca, Caracteristicas_Raca, form=Caracteristicas_RacaForm, extra=1, can_delete=False )
        caracteristicas_form = caracteristicas_factory_form(request.POST)
        if form.is_valid() and caracteristicas_form.is_valid():
            raca = form.save()
            caracteristicas_form.instance = raca
            caracteristicas_form.save()
            return HttpResponseRedirect(reverse_lazy('fichas:raca_list'))
        else:
            context = {
                'raca': form,
                'caracteristicas': caracteristicas_form,
            }
            return render(request, template_name, context)
# Listar Todas as Raças
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def list_Raca(request):
    template_name ='cad_pet/raca_list.html'
    raca = Raca.objects.all()
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)
# Atualizar/Alterar Raças
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def update_Raca(request, pk):
    template_name = 'cad_pet/raca_update.html'
    obj_raca =  Raca.objects.get(id=pk)
    if request.method == 'GET':
        form = RacaForm(instance=obj_raca)
        context = { 'form': form }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = RacaForm(request.POST, instance=obj_raca)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:raca_list'))
        else:
            context = { 'form': form}
            return render(request, template_name, context=context)
# Deletar uma Raça
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def delete_Raca(request, pk):
    obj = Raca.objects.get(id=pk)
    obj.delete()

    return HttpResponseRedirect(reverse('fichas:raca_list'))

#Select Espécie e Raça Add Pet por um funcionário
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def load_funcoes(request):
    template_name = 'pet/funcao_ajax.html'
    especie_id = request.GET.get('id_especie')
    raca = Raca.objects.filter(especie=especie_id)
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)
# Select Espécie e Raça Add Pet por um Cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def load_cliente(request):
    template_name = 'pet/cliente_ajax.html'
    especie_id = request.GET.get('id_pet_set-0-especie')
    raca = Raca.objects.filter(especie=especie_id)
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)
# Select Espécie e Raça Add Pet por um Cliente
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def load_update_pet(request):
    template_name = 'pet/update_pet_ajax.html'
    especie_id = request.GET.get('id_especie')
    raca = Raca.objects.filter(especie=especie_id)
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)
