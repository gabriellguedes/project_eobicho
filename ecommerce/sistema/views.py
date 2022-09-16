from django.shortcuts import render, resolve_url
from .forms import RacaForm, EspecieForm
from .models import Raca, Especie
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.views.generic import UpdateView


# Add Espécie/Raça 
def especie_add(request):
    template_name = 'cad_pet/especie_add_form.html'
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
            url = 'sys:list_Especie'
            return HttpResponseRedirect(resolve_url(url))
    else:
        form = EspecieForm(instance=especie_form, prefix='main')
        formset = raca_formset(instance=especie_form, prefix='estoque')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)

# Adicionar uma nova Especie
def add_Especie(request):
	template_name = 'cad_pet/especie_add.html'
	form = EspecieForm(request.POST or None)
	if request.method=='POST':
		if form.is_valid():
			form = form.save()
			return HttpResponseRedirect(reverse('sys:list_Especie'))
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
	
	return HttpResponseRedirect(reverse('sys:list_Especie'))

# Atualizar/Alterar Espécies
class update_Especie(UpdateView):
	template_name = 'cad_pet/especie_update.html'
	model = Especie
	fields = '__all__'
	success_url = reverse_lazy('sys:list_Especie')

# Adicionar Raça
def add_Raca(request):
	template_name = 'cad_pet/raca_add.html'
	form = RacaForm(request.POST)
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy('sys:list_Raca'))
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
	success_url = reverse_lazy('sys:list_Raca')

# Deletar uma Raça
def delete_Raca(request, pk):
	obj = Raca.objects.get(id=pk)
	obj.delete()

	return HttpResponseRedirect(reverse('core:list_Raca'))


