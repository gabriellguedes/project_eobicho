from django.shortcuts import render
from .models import Ficha
from .forms import FichaForm

def new_ficha(request, pk):
	template_name='banho/new_ficha.html'

	if request.method == 'GET':
		form = FichaForm()
		context = {'form': form}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = FichaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pet:pet_detail', kwargs={'pk': pk}))
		else:
			context = {'form': form}
			return render(request, template_name, context=context)
