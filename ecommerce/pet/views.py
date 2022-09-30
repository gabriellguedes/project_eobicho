from django.shortcuts import render, resolve_url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from ecommerce.accounts.models import Cliente
from ecommerce.accounts.forms import ClienteForm
from ecommerce.ficha.models import Ficha
from ecommerce.ficha.forms import FichaForm
from .forms import PetForm, PesoForm, RacaForm, EspecieForm
from .models import Pet, Peso, Raca, Especie
from django.views.generic import UpdateView

# Cadastrar Pet - Feito por funcionário
def pet_add(request):
    template_name = 'pet/pet_add.html'
    especie = Especie.objects.all().order_by('especie')
    raca = []

    if request.method == 'GET':
        form = PetForm()
        context = {
            'form': form,
            'especie': especie,
            'raca': raca,
            }
        return render(request, template_name, context=context)
    elif request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pet:pet_list'))
        else:
            context = { 'form': form }
            return render(request, template_name, context=context)

#Cadastro Pet feito pelo cliente 
def cliente_pet_add(request, pk):
    template_name = 'pet/cliente_pet_add.html'
    obj = Cliente.objects.get(id=pk)
    especie = Especie.objects.all().order_by('especie')
    raca = []

    if request.method == 'GET':
        form = ClienteForm()

        form_pet_factory = inlineformset_factory(Cliente, Pet, form=PetForm, extra=1)
        form_pet = form_pet_factory()

        context = {
            'especie': especie,
            'raca': raca,
            'form': form_pet,
            'cliente': obj,
        }
        return render(request, template_name, context=context)

    elif request.method == 'POST':
        form = ClienteForm(request.POST)
        form_pet_factory = inlineformset_factory(Cliente, Pet, form=PetForm)
        form_pet = form_pet_factory(request.POST, request.FILES)
               
        if form_pet.is_valid():
            form_pet.instance = obj
            form_pet.save()
            return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={"pk": obj.pk}))
        else:
            context = {
                'especie': especie,
                'raca': raca,
                'form': form_pet,
                'cliente': obj,
            }
            return render(request, template_name, context=context)

#Lista de Exibição Paginação
def paginacao(request):
    template_name = 'pet/pet_list.html'
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '5')
    
    if not (parametro_limit.isdigit() and int(parametro_limit)>0):
        parametro_limit = '10'

    pets = Pet.objects.get_queryset().order_by('id')
    pets_paginator = Paginator(pets, parametro_limit)

    objects = Pet.objects.all()
    
  
    try:
        page = pets_paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = pets_paginator.page(1)
       

    context = {
        'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'pets': page,
        'object_list':objects
    }
    return render(request, template_name, context=context)

#Vizualizar Pet e Ficha
def detailPet(request, pk):
    template_name ='pet/pet_detail.html'
    obj = Pet.objects.get(id=pk)
    ficha = obj.fichaPets.last()
    last_fichas = obj.fichaPets.all()
    # Listar Peso        
    list_peso = Peso.objects.filter(pet=obj.pk)    
    
    # Add Peso
    if request.method == 'GET':
        form = PetForm()
        form_peso_factory = inlineformset_factory(Pet, Peso, form=PesoForm, extra=1)
        form_peso = form_peso_factory()

        context={
            'pet': obj,
            'ficha': ficha,
            'last_fichas': last_fichas,
            'peso': form_peso,
            'listpeso': list_peso,
        }
        return render(request, template_name, context=context)
        
    elif request.method == 'POST':
        form = PetForm(request.POST)
        form_peso_factory = inlineformset_factory(Pet, Peso, form=PesoForm)
        form_peso = form_peso_factory(request.POST)
        
        if form_peso.is_valid():
            form_peso.instance = obj
            form_peso.save()
            return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={"pk": obj.pk}))
        else:
           
            context = { 
                'pet': obj,
                'ficha': ficha,
                'last_fichas': last_fichas,
                'peso': form_peso,
                'listpeso': list_peso,
             }
            return render(request, template_name, context=context) 

#Atualização
def pet_update(request, pk):
    template_name = 'pet/pet_update.html'
    obj = Pet.objects.get(id=pk)

    if request.method == 'GET':
        form = PetForm(instance=obj)
        context = {'form_pet': form}
        return render(request, template_name, context=context)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={"pk": obj.pk}))
        else:
            context = { 'form_pet': form }
            return render(request, template_name, context=context)

# Add Espécie/Raça 
def especie_add(request):
    template_name = 'cad_pet/especie_add_form.html'
    
    if request.method == 'GET':
        form = EspecieForm()
        form_raca_factory = inlineformset_factory(Especie, Raca, form=RacaForm, extra=3)
        form_raca = form_raca_factory()

        context = {
            'form': form,
            'form_raca': form_raca,
        }
        return render(request, template_name, context=context)

    elif request.method == 'POST':
        form = EspecieForm(request.POST)
        form_raca_factory = inlineformset_factory(Especie, Raca, form=RacaForm, extra=3)
        form_raca = form_raca_factory(request.POST)
        
        if form.is_valid() and form_raca.is_valid():
            especie = form.save()
            form_raca.instance = especie
            form_raca.save()
            return HttpResponseRedirect(reverse('pet:especie_list'))
        else:
            context = {
             'form': form,
             'form_raca': form_raca
            }
            return render(request, template_name, context=context)

# Adicionar uma nova Especie
def add_Especie(request):
    template_name = 'cad_pet/especie_add.html'
    form = EspecieForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(reverse('pet:especie_list'))
    context ={'especie': form}      
    return render(request, template_name, context=context)

# Listar as Especies
def list_Especie(request):
    template_name = 'cad_pet/especie_list.html'
    obj = Especie.objects.all()
    context = { 'especie': obj }
    return render(request, template_name, context=context)

# Deletar uma Especie
def delete_Especie(request, pk):
    obj = Especie.objects.get(id=pk)
    obj.delete()
    
    return HttpResponseRedirect(reverse('pet:especie_list'))

# Atualizar/Alterar Espécies
class update_Especie(UpdateView):
    template_name = 'cad_pet/especie_update.html'
    model = Especie
    fields = '__all__'
    success_url = reverse_lazy('pet:especie_list')

# Adicionar Raça
def add_Raca(request):
    template_name = 'cad_pet/raca_add.html'
    form = RacaForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('pet:raca_list'))
    context = {
        'raca': form,
    }
    return render(request, template_name, context)

# Listar Todas as Raças
def list_Raca(request):
    template_name ='cad_pet/raca_list.html'
    raca = Raca.objects.all()
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)

# Atualizar/Alterar Raças
class update_Raca(UpdateView):
    template_name = 'cad_pet/raca_update.html'
    model = Raca
    fields = '__all__'
    success_url = reverse_lazy('pet:raca_list')

# Deletar uma Raça
def delete_Raca(request, pk):
    obj = Raca.objects.get(id=pk)
    obj.delete()

    return HttpResponseRedirect(reverse('core:raca_list'))

#Select Espécie e Raça Add Pet por um funcionário
def load_funcoes(request):
    template_name = 'pet/funcao_ajax.html'
    especie_id = request.GET.get('id_especie')
    raca = Raca.objects.filter(especie=especie_id)
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)
# Select Espécie e Raça Add Pet por um Cliente
def load_cliente(request):
    template_name = 'pet/cliente_ajax.html'
    especie_id = request.GET.get('id_pet_set-0-especie')
    raca = Raca.objects.filter(especie=especie_id)
    context = {
        'raca': raca,
    }
    return render(request, template_name, context=context)

