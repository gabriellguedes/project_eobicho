from django.contrib import admin
from .models import PetModel, AnamneseModel

admin.site.register(PetModel)
admin.site.register(AnamneseModel)

admin.register(PetModel)
class PetAdmin(admin.ModelAdmin):
	list_display = (
		'__str__',
		'nome',  
	'apelido', 
	'aniversario', 
	'idade',
	'peso',
	'tamanho', 	
	'especie',
	'racaCachorro',
	'racaGato',
	'temperamentongth',
	'pelagem', 
	'type_pelo', 
	'coloracao', 
	'caracteristicas'

	)
	search_fields = ('nome')
	list_filter = ('especie')

admin.register(AnamneseModel)
class AnamneseAdmin(admin.ModelAdmin):
	model = AnamneseModel
	extra = 0