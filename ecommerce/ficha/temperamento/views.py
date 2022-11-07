from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Temperamento
from .forms import TemperamentoForm

# Adicionar Temperamento
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def temperamento_add(request):
	template_name = 'temperamento/temperamento_add.html'
	if request.method == 'GET':
		form = TemperamentoForm()
		context = {'form': form}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = TemperamentoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('fichas:temperamento:temperamento_list'))
		else:
			context={'form':form}
			return render(request, template_name, context=context)
# Listar Temperamentos Cadastrados
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def temperamento_list(request):
	template_name = 'temperamento/temperamento_list.html'
	obj = Temperamento.objects.all()
	context={'form':obj}
	return render(request, template_name, context=context)
# Atualizar/Alterar um Temperamento Cadastrado
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def temperamento_update(request, pk):
	template_name = 'temperamento/temperamento_update.html'
	obj = Temperamento.objects.get(id=pk)
	if request.method == 'GET':
		form = TemperamentoForm(instance=obj)
		context = {'form': form}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = TemperamentoForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('fichas:temperamento:temperamento_list'))
		else:
			context = {'form':form}
			return render(request, template_name, context=context)
# Deletar um Temperamento cadastrado
@login_required(redirect_field_name='Acesso_Negado', login_url='core:permission')
def temperamento_delete(request, pk):
	template_name = 'temperamento/temperamento_delete.html'
	objeto = Temperamento.objects.get(id=pk)
	if request.method == 'GET':
		context ={'form':objeto}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		objeto.delete()
		return HttpResponseRedirect(reverse('fichas:temperamento:temperamento_list'))

