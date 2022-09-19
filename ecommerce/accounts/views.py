
from django.shortcuts import render
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from .models import Cliente
from .forms import ClienteForm

def home(request):
	template = 'accounts/home.html'
	return render(request, template)
# Add Cliente 
def cliente_add(request):
	template_name = 'clientes/cliente_add.html'
	form = ClienteForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('contas:cliente_list'))
	context = {'form': form	}
	return render(request, template_name, context=context)

# Listar Cliente
def cliente_list(request):
	template_name = 'clientes/cliente_list.html'
	parametro_page = request.GET.get('page', '1')
	parametro_limit = request.GET.get('limit', '5')

	if not (parametro_limit.isdigit() and int(parametro_limit)>0):
		parametro_lim

	clientes = Cliente.objects.get_queryset().order_by('id')
	clientes_paginator = Paginator(clientes, parametro_limit)

	lista = Cliente.objects.all()

	try:
		page = clientes_paginator.page(parametro_page)

	except (EmptyPage, PageNotAnInteger):
		page = clientes_paginator.page(1)


	context = {
		'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'clientes': page,
		'lista': lista,
	}
	return render(request, template_name, context=context)

# Atualização
class cliente_update(UpdateView):
    template_name = 'clientes/cliente_update.html'
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('contas:cliente_list')

# Deletar
#Apagar    
class cliente_delete(DeleteView):
	template_name = 'clientes/cliente_delete.html'
	queryset = Cliente.objects.all()
	success_url = reverse_lazy('contas:cliente_list')