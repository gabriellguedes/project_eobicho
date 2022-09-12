from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ecommerce.pet.models import Pet
from .models import Ficha
from .forms import FichaForm
from ecommerce.pet.forms import PetForm
from django.forms import inlineformset_factory

# Criar uma nova ficha
def createFicha(request, pk):
    template_name = 'anamnese.html'
    pet_pk = Pet.objects.get(pk=pk)
    
    if request.method == 'GET':
        form = FichaForm()
        context = {
            'form':form
        }
        return render(request, template_name, context=context)
    else:
        form = FichaForm(request.POST)
        if form.is_valid():
            form.pet == pet_pk
            pet = form.save()
            return HttpResponseRedirect(reverse('pet:list'))
        context = {
            'form':form
        }

        return render(request, template_name, context=context)


#Listar todas as fichas cadastradas
def listFicha(request):
    template_name = 'ficha_list.html'
    lista = Ficha.objects.all()
    context = { 'lista': lista}
    return render(request, template_name, context)

#Visualizar ficha antiga
def detailFicha(request, pk, n):
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