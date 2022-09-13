from django.contrib import admin
from .models import Pet, Especie, Raca

admin.site.register(Pet)

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
	list_display = ('__str__',)
	search_fields = ('especie',)

@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
	list_display = ('__str__',)
	search_fields = ('raca',)


