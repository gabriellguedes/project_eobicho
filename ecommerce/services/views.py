from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.forms import inlineformset_factory
from django.urls import reverse
from django.http import HttpResponseRedirect
from ecommerce.pet.models import Pet
from ecommerce.ficha.models import Anamnese
from ecommerce.ficha.forms import AnamneseForm
from .models import Ficha, Banho, Tosa, Itens
from .forms import FichaForm, BanhoForm, TosaForm, ItensForm

# Adicionar um tipo de banho
def banho_add(request):
	template_name = 'banho/banho_add.html'
	if request.method == 'GET':
		form = BanhoForm()
		return render(request, template_name, {'form':form})
	elif request.method == 'POST':
		form = BanhoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:banho_list'))
		else:
			return render(request, template_name, {'form':form})
# Atualizar um tipo de banho
def banho_update(request, pk):
	template_name ='banho/banho_update.html'
	objeto = Banho.objects.get(id=pk)
	if request.method =='GET':
		form = BanhoForm(instance=objeto)
		return render(request, template_name, {'form':form})
	elif request.method=='POST':
		form = BanhoForm(request.POST, instance=objeto)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:banho_list'))
		else:
			return render(request, template_name, {'form': form})
# Listar os banhos cadastrados
def banho_list(request):
	template_name = 'banho/banho_list.html'
	obj = Banho.objects.all()
	return render(request, template_name, {'form': obj})
# Deletar um banho
def banho_delete(request, pk):
	template_name = 'banho/banho_delete.html'
	objeto = Banho.objects.get(id=pk)
	if request.method == 'GET':
		return render(request, template_name, {'form': objeto})
	elif request.method == 'POST':
		objeto.delete()
		return HttpResponseRedirect(reverse('services:banho_list'))
# Adicionar um novo tipo de Tosa
def tosa_add(request):
	template_name = 'tosa/tosa_add.html'
	if request.method == 'GET':
		form = TosaForm()
		return render(request, template_name, {'form':form})
	elif request.method == 'POST':
		form = TosaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:tosa_list'))
		else:
			return render(request, template_name, {'form':form})
# Atualizar um tipo de Tosa			
def tosa_update(request, pk):
	template_name ='tosa/tosa_update.html'
	objeto = Tosa.objects.get(id=pk)
	if request.method =='GET':
		form = TosaForm(instance=objeto)
		return render(request, template_name, {'form':form})
	elif request.method=='POST':
		form = TosaForm(request.POST, instance=objeto)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:tosa_list'))
		else:
			return render(request, template_name, {'form': form})
# Listar os tipos de Tosa cadastrados			
def tosa_list(request):
	template_name = 'tosa/tosa_list.html'
	obj = Tosa.objects.all()
	return render(request, template_name, {'form': obj})
# Deletar um tipo de Tosa
def tosa_delete(request, pk):
	template_name = 'tosa/tosa_delete.html'
	objeto = Tosa.objects.get(id=pk)
	if request.method == 'GET':
		return render(request, template_name, {'form': objeto})
	elif request.method == 'POST':
		objeto.delete()
		return HttpResponseRedirect(reverse('services:tosa_list'))
# Adicionar um Item/pertence do Animal
def itens_add(request):
	template_name = 'itens/itens_add.html'
	if request.method == 'GET':
		form = ItensForm()
		return render(request, template_name, {'form':form})
	elif request.method == 'POST':
		form = ItensForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:itens_list'))
		else:
			return render(request, template_name, {'form':form})
# Atualizar um Item/pertence do Animal		
def itens_update(request, pk):
	template_name ='itens/itens_update.html'
	objeto = Itens.objects.get(id=pk)
	if request.method =='GET':
		form = ItensForm(instance=objeto)
		return render(request, template_name, {'form':form})
	elif request.method=='POST':
		form = ItensForm(request.POST, instance=objeto)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('services:itens_list'))
		else:
			return render(request, template_name, {'form': form})
# Listar itens/pertences do Animal			
def itens_list(request):
	template_name = 'itens/itens_list.html'
	obj = Itens.objects.all()
	return render(request, template_name, {'form': obj})
# Apagar um Item ou pertence do animal
def itens_delete(request, pk):
	template_name = 'itens/itens_delete.html'
	objeto = Itens.objects.get(id=pk)
	if request.method == 'GET':
		return render(request, template_name, {'form': objeto})
	elif request.method == 'POST':
		objeto.delete()
		return HttpResponseRedirect(reverse('services:itens_list'))

# Nova Ficha para realização do Banho e Tosa Pet Agendado
def new_ficha(request, pk):
	template_name='ficha/new_ficha.html'
	today = datetime.date(datetime.utcnow())
	pet = Pet.objects.get(id=pk)
	anamnese = Anamnese.objects.filter(pet=pet).last()

	if request.method == 'GET':
		form = FichaForm()
		form_pet_factory = inlineformset_factory(Pet, Ficha, form=FichaForm, extra=1, can_delete=False)
		form_pet = form_pet_factory()

		form_anamnese_factory = inlineformset_factory(Ficha, Anamnese, form=AnamneseForm, extra=1, can_delete=False)
		form_anamnese = form_anamnese_factory()

		context = {
			'form': form_pet,
			'anamnese': anamnese,
			'pet': pet,
			'today': today,
			
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = FichaForm(request.POST)

		form_pet_factory = inlineformset_factory(Pet, Ficha, form=FichaForm, extra=1, can_delete=False)
		form_pet = form_pet_factory(request.POST)
		
		form_anamnese_factory = inlineformset_factory(Ficha, Anamnese, form=AnamneseForm, extra=1, can_delete=False)
		form_anamnese = form_anamnese_factory(request.POST)

		if form_pet.is_valid():
			form_pet.instance = pet
			new_banho = form_pet.save(commit=False)
			new_banho[0].funcionario = request.user
			new_banho[0].status = 'aguardando'
			new_banho[0].save()
			form_pet.save()
			return HttpResponseRedirect(reverse('services:list_ficha'))
		else:

			context = {
				'form': form_pet,
				'anamnese': anamnese,
				'pet': pet,
				'today': today,
				'class':'alert alert-warning',
				'msg':'Atenção - Ficha para realização do Banho e Tosa não foi criada, verifique se todos os campos foram preenchidos corretamente.',
				
			}
			return render(request, template_name, context=context)
# Nova Ficha para realizar o Banho e Tosa Pet não agendado.
def add_ficha(request):
	template_name='ficha/add_ficha.html'
	context={}
	if request.method == 'GET':
		return render(request, template_name)
	elif request.method == 'POST':
		try:
			search = request.POST['SelectPet']
			pet = Pet.objects.get(id=search)
		except ValueError:
			context['msg'] = 'O Id do Pet é composto apenas por números.'
			context['class'] = 'alert alert-info'
			return render(request, template_name, context=context)
		except ObjectDoesNotExist:
			context['msg'] = 'Id não existe!'
			context['class'] = 'alert alert-info'
			return render(request, template_name, context=context)
		return HttpResponseRedirect(reverse('services:new_ficha', kwargs={'pk': search}))	
# Vizualizar Ficha de Banho e Tosa Cadastrada
def detail_ficha(request, pk):
	template_name = 'ficha/detail_ficha.html'
	ficha = Ficha.objects.get(id=pk)
	pet = Pet.objects.get(id=ficha.pet.id)
	anamnese = Anamnese.objects.filter(pet=pet).last()
	context = {
		'form': ficha,
		'pet': pet,
		'anamnese': anamnese,
	}
	return render(request, template_name, context=context)	
# Listar todos as Fichas de Banho e Tosa Cadastradas
def list_ficha(request):
	template_name = 'ficha/list_ficha.html'
	fichas_atendendo = Ficha.objects.filter(status='atendendo')
	fichas_aguardando = Ficha.objects.filter(status='aguardando')
	fichas_aprovado = Ficha.objects.filter(status='aprovado')
	fichas_alterado = Ficha.objects.filter(status='alterado')
	fichas_cancelado = Ficha.objects.filter(status='cancelado')
	fichas_finalizado = Ficha.objects.filter(status='finalizado')
	context = {
		'atendendo': fichas_atendendo,
		'aguardando': fichas_aguardando,
		'aprovado': fichas_aprovado,
		'alterado': fichas_alterado,
		'cancelado': fichas_cancelado,
		'finalizado': fichas_finalizado,
	}
	return render(request, template_name, context=context)
# Apagar ficha de banho e tosa
def delete_ficha(request, pk):
	template_name='ficha/delete_ficha.html'
	ficha = Ficha.objects.get(id=pk)
	if request.method == 'GET':
		context ={'form':ficha}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		ficha.delete()
		return HttpResponseRedirect(reverse('services:list_detail')) 
# Pag q o cliente 
def permission_tutor(request, pk):
	template_name = 'ficha/permission_tutor.html'

	pet = Pet.objects.get(id=pk)
	objeto = Ficha.objects.filter(pet=pet)
	try:
		ficha = objeto.get(status='aguardando')
	except ObjectDoesNotExist:
		ficha = ''
	anamnese = Anamnese.objects.filter(pet=pet).last()

	if request.method == 'GET':
		context = {
			'form': ficha,
			'pet': pet,
			'anamnese': anamnese,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		ficha.status = 'aprovado'
		ficha.save()
		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': request.user.id}))
# Vizualizar Ficha de Banho e Tosa Cadastrada completa para o Tutor
def detail_ficha_tutor(request, pk):
	template_name = 'ficha/detail_ficha_tutor.html'
	ficha = Ficha.objects.get(id=pk)
	pet = Pet.objects.get(id=ficha.pet.id)
	anamnese = Anamnese.objects.filter(pet=pet).last()
	context = {
		'form': ficha,
		'pet': pet,
		'anamnese': anamnese,
	}
	return render(request, template_name, context=context)
# Nega permissão para banho e tosa
def permission_ficha_cancelada(request, pk):
	ficha = Ficha.objects.get(id=pk)
	ficha.status = 'cancelado'
	ficha.save()
	return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': request.user.id}))
# Atendimento para o banho e tosa
def atender_ficha(request, pk):
	ficha = Ficha.objects.get(id=pk)
	ficha.status = 'atendendo'
	ficha.save()
	return HttpResponseRedirect(reverse('services:list_ficha'))

# Finalizar Atendimento para o banho e tosa
def finalizar_ficha(request, pk):
	ficha = Ficha.objects.get(id=pk)
	ficha.status = 'finalizado'
	ficha.save()
	return HttpResponseRedirect(reverse('services:list_ficha'))
