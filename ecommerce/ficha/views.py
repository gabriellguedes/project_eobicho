from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ecommerce.pet.models import Pet
from .models import Ficha, Pele, Doenca, Ectoparasitas, Infec_pele, Pelos, Estado_pelos, Condicao_pelos, Boca, Unhas, Olhos, Orelhas, Patas
from .forms import FichaForm, PeleForm, DoencaForm, EctoparasitasForm, Infec_peleForm, PelosForm, Estado_pelosForm, Condicao_pelosForm, BocaForm, UnhasForm, OlhosForm, OrelhasForm, PatasForm
from ecommerce.pet.forms import PetForm
from django.forms import inlineformset_factory

# Criar uma nova ficha
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
            form_ficha.instance = obj
            form_ficha.funcionario = request.user    
            form_ficha.save()
            return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={"pk": obj.pk}))
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

# Adicionar Ectoparasitas
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
def ectoparasitas_list(request):
    template_name = 'itens_ficha/pele/ectoparasitas_list.html'
    objeto = Ectoparasitas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Update ectoparasitas
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
def ectoparasitas_delete(request, pk):
    objeto = Ectoparasitas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:ectoparasitas_list'))
    else:
        context = {'form':form}
        return render(request, context=context)

# Add infec_pele
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
def infec_pele_list(request):
    template_name = 'itens_ficha/pele/infec_pele_list.html'
    objeto = Infec_pele.objects.all()
    context = {'form': objeto}
    return render(request, template_name, context=context)
# Atualizar infec_pele
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
def infec_pele_delete(request, pk):
    objeto = Infec_pele.objects.get(id=pk)
    if objeto != '':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:infec_pele_list'))
    else:
        msg = 'Item não existe!'
        context = {'msg': msg }
        return render(request, context=context)    

# Adicionar Novo Tipo de Pelos
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
def pelos_list(request):
    template_name='itens_ficha/pelos/pelos_list.html'
    objeto = Pelos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar Tipo de pelo cadastrada
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
def pelos_delete(request, pk):
    objeto = Pelos.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:pelos_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)
   

# Adicionar Novo condição de Pelos
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
def estado_pelos_list(request):
    template_name='itens_ficha/pelos/estado_pelos_list.html'
    objeto = Estado_pelos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar condição do pelo cadastrada
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
def estado_pelos_delete(request, pk):
    objeto = Estado_pelos.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:estado_pelos_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)
   

# Adicionar Novo Tipo de Pelos
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
def condicao_pelos_list(request):
    template_name='itens_ficha/pelos/condicao_pelos_list.html'
    objeto = Condicao_pelos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar Tipo de pelo cadastrada
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
def condicao_pelos_delete(request, pk):
    objeto = Condicao_pelos.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:condicao_pelos_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)
   

#Boca 
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
def boca_list(request):
    template_name='itens_ficha/boca/boca_list.html'
    objeto = Boca.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar boca cadastrada
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
def boca_delete(request, pk):
    objeto = Boca.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:boca_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)
   
#Unhas 
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
def unhas_list(request):
    template_name='itens_ficha/unhas/unhas_list.html'
    objeto = Unhas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar unhas cadastrada
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
def unhas_delete(request, pk):
    objeto = Unhas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:unhas_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)

#Olhos 
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
def olhos_list(request):
    template_name='itens_ficha/olhos/olhos_list.html'
    objeto = Olhos.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar boca cadastrada
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
def olhos_delete(request, pk):
    objeto = Olhos.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:olhos_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)

#Orelhas 
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
def orelhas_list(request):
    template_name='itens_ficha/orelhas/orelhas_list.html'
    objeto = Orelhas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar orelhas cadastrada
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
def orelhas_delete(request, pk):
    objeto = Orelhas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:orelhas_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)

#Patas
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
def patas_list(request):
    template_name='itens_ficha/patas/patas_list.html'
    objeto = Patas.objects.all()
    context = {
        'form': objeto
    }
    return render(request, template_name, context=context)
# Atualizar patas cadastrada
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
def patas_delete(request, pk):
    objeto = Patas.objects.get(id=pk)
    if objeto != None:
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:patas_list')) 
    else:
        msg = 'Item não encotrado'
        context = {'msg': msg}
        return render(request, context=context)