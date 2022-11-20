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

# Add Espécie/Raça
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission') 
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def especie_add(request):
    template_name = 'especie_add.html'
    
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
            return HttpResponseRedirect(reverse('fichas:especie:especie_list'))
        else:
            context = {
             'form': form,
             'form_raca': form_raca
            }
            return render(request, template_name, context=context)
# Adicionar uma nova Especie
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def add_Especie(request):
    template_name = 'especie_add.html'
    form = EspecieForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(reverse('fichas:especie:especie_list'))
    context ={'form': form}      
    return render(request, template_name, context=context)
# Listar as Especies
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def list_Especie(request):
    template_name = 'especie_list.html'
    obj = Especie.objects.all()
    context = { 'especie': obj }
    return render(request, template_name, context=context)
# Deletar uma Especie
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def delete_Especie(request, pk):
    template_name = 'especie_delete.html'
    objeto  = Especie.objects.get(id=pk)
    if request.method == 'GET':
        context ={'form':objeto}
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        objeto.delete()
        return HttpResponseRedirect(reverse('fichas:especie:especie_list'))
    
    return HttpResponseRedirect(reverse('fichas:especie:especie_list'))
# Atualizar/Alterar Espécies
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
@has_permission_decorator('view_funcionario', redirect_to_login='core:permission')
def update_Especie(request, pk):
    template_name = 'especie_update.html'
    obj_especie = Especie.objects.get(id=pk)
    if request.method == 'GET':
        form = EspecieForm(instance=obj_especie)
        context = { 'form': form }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = EspecieForm(request.POST, instance=obj_especie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichas:especie:especie_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)
