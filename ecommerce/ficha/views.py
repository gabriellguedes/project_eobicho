from django.shortcuts import render
from ecommerce.pet.models import Pet
from .models import Ficha
from .forms import FichaForm

# Criar uma nova ficha
def createFicha(request, pk):
    template_name = 'anamnese.html'
    pet = Pet.objects.get(id=pk)
    ficha = pet.fichaPets.create()
    fields = 'pet'

    if request.method == 'GET':
        form =  FichaForm()
        context = {
            'form':form
        }
        return render(request, template_name, context=context)
    else:
        form =  FichaForm(request.POST)
        if form.is_valid():
            pet = form.save()
            form =  FichaForm()

        context = {
            'form':form,
            'formset': ficha,
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