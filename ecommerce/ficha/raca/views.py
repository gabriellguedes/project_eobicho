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

# Adicionar Raça
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def add_Raca(request):
    template_name = 'raca/raca_add.html'
    if request.method == 'GET':

        form = RacaForm()
        caracteristicas_factory_form = inlineformset_factory(Raca, Caracteristicas_Raca, form=Caracteristicas_RacaForm, extra=1, can_delete=False )
        caracteristicas_form = caracteristicas_factory_form()
        context = { 
            'raca': form,
            'caracteristicas': caracteristicas_form,
        }
        return render(request, template_name, context=context)
    elif request.method=='POST':        
        form = RacaForm(request.POST)
        caracteristicas_factory_form = inlineformset_factory(Raca, Caracteristicas_Raca, form=Caracteristicas_RacaForm, extra=1, can_delete=False )
        caracteristicas_form = caracteristicas_factory_form(request.POST)
        if form.is_valid() and caracteristicas_form.is_valid():
            raca = form.save()
            caracteristicas_form.instance = raca
            caracteristicas_form.save()
            return HttpResponseRedirect(reverse('fichas:raca:raca_list'))
        else:
            context = {
                'raca': form,
                'caracteristicas': caracteristicas_form,
            }
            return render(request, template_name, context)
# Listar Todas as Raças
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def list_Raca(request):
    template_name ='raca/raca_list.html'
    raca = Raca.objects.all()
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)

# Atualizar/Alterar Raças
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def update_Raca(request, pk):
    template_name = 'raca/raca_update.html'
    obj_raca =  Raca.objects.get(id=pk)
    if request.method == 'GET':
        form = RacaForm(instance=obj_raca)
        caracteristicas_factory_form = inlineformset_factory(Raca, Caracteristicas_Raca, form=Caracteristicas_RacaForm, extra=0, can_delete=False )
        caracteristicas_form = caracteristicas_factory_form(instance=obj_raca)
        context = { 
            'raca': form,
            'caracteristicas': caracteristicas_form,

        }
        return render(request, template_name, context=context)
    
    elif request.method == 'POST':
        form = RacaForm(request.POST, instance=obj_raca)
        caracteristicas_factory_form = inlineformset_factory(Raca, Caracteristicas_Raca, form=Caracteristicas_RacaForm, extra=0, can_delete=False )
        caracteristicas_form = caracteristicas_factory_form(request.POST, instance=obj_raca)
        if form.is_valid() and caracteristicas_form.is_valid():
            raca = form.save()
            caracteristicas_form.instance = raca
            caracteristicas_form.save()
            return HttpResponseRedirect(reverse('fichas:raca:raca_list'))
        else:
            context = { 
                'raca': form,
                'caracteristicas': caracteristicas_form,
            }
            return render(request, template_name, context=context)
# Deletar uma Raça
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def delete_Raca(request, pk):
    template_name = 'raca/raca_delete.html'
    objeto = Raca.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:raca:raca_list'))