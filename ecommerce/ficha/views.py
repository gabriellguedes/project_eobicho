from django.shortcuts import render
from ecommerce.pet.models import Pet
from .models import Ficha
from .forms import FichaForm
from ecommerce.pet.forms import PetForm
from django.forms import inlineformset_factory

# Criar uma nova ficha
def createFicha(request, pk):
    template_name = 'form_add.html'
    pet_form = Pet()
    a_form = inlineformset_factory(
        Pet,
        Ficha,
        form= FichaForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form= PetForm(request.POST, instance=pet_form, prefix='main')
        formset= a_form(
            request.POST,
            instance=pet_form, 
            prefix='pet',
        )
        if form.is_valid() and formset.is_valid():
            form=form.save(commit=False)
            formset.funcionario = request.user
            formset.status = status
            formset.pet= Pet.objects.get(id=pk)
            form.save()
            formset.save()

            url = 'pet:detail'
            return { 'pk': form.pk}
    else:
        form= PetForm(instance=pet_form, prefix='main')
        formset= a_form(instance=pet_form, prefix='pet')
    context={
        'form': form,
        'formset': formset
    }    
    return render(request, template_name, context)   

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