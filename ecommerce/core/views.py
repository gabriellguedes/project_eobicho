from django.shortcuts import render
from .forms import RacaForm, EspecieForm
from ecommerce.pet.models import Raca, Especie
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory

def login(request):
	template_name = 'index.html'
	return render(request, template_name)

# Add Espécie/Raça 
def especie_add(request):
    template_name = 'core/especie_add_form.html'
    especie_form = Especie()
    raca_formset = inlineformset_factory(
        Especie,
        Raca,
        form=RacaForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = EspecieForm(request.POST, instance=especie_form, prefix='main')
        formset = raca_formset(
            request.POST,
            instance=especie_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            url = 'estoque:estoque_entrada_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EspecieForm(instance=especie_form, prefix='main')
        formset = raca_formset(instance=especie_form, prefix='estoque')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)

# Adicionar uma nova Especie
def add_Especie(request):
	template_name = 'core/add_form.html'
	form = EspecieForm(request.POST or None)
	if request.method=='POST':
		if form.is_valid():
			form = form.save()
			return HttpResponseRedirect(reverse('core:list_Especie'))
	context ={'especie': form}		
	return render(request, template_name, context=context)

# Listar as Especies
def list_Especie(request):
	template_name = 'core/list_especie.html'
	obj = Especie.objects.all()
	context = { 'especie': obj }
	return render(request, template_name, context=context)

# Deletar uma Especie
def delete_Especie(request, pk):
	obj = Especie.objects.get(id=pk)
	obj.delete()
	
	return HttpResponseRedirect(reverse('core:list_Especie'))

# Atualizar/Alterar Espécies
def update_Especie(request, pk):
	template_name = 'update_especie.html'
	obj = Especie.objects.get(id=pk)
	context = {
		'especie': obj,
	}
	return render(request, template_name, context=context)

# Adicionar Raça
def add_Raca(request):
	template_name = 'core/add_raca_form.html'
	form = RacaForm(request.POST)
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy('core:list_Raca'))
	context = {
		'raca': form,
	}
	return render(request, template_name, context)

# Listar Todas as Raças
def list_Raca(request):
	template_name ='core/list_raca.html'
	raca = Raca.objects.all()
	context = {
		'raca': raca,
	}
	return render(request, template_name, context=context)

# Atualizar/Alterar Raças
def update_Raca(request, pk):
	template_name = 'core/update_raca.html'
	obj = Raca.objects.get(id=pk)
	context = {
		'raca': obj,
	}
	return render(request, template_name, context=context)

# Deletar uma Raça
def delete_Raca(request, pk):
	obj = Raca.objects.get(id=pk)
	obj.delete()

	return HttpResponseRedirect(reverse('core:list_Raca'))

