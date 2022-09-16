from django.urls import path
from . import views

app_name = 'sys'

urlpatterns = [
# Especies
	path('add-especie/', views.especie_add, name='especie_add'),
	path('addespecie/', views.add_Especie, name='add_Especie'),
	path('listEspecie/', views.list_Especie, name='especie_list'),
	path('delete-Especie/<int:pk>/', views.delete_Especie, name='especie_delete'),
	path('update-Especie/<int:pk>/', views.update_Especie.as_view(), name='especie_update'),
	# Raças
	path('add-raca/', views.add_Raca, name='raca_add'),
	path('list-Raca/', views.list_Raca, name='raca_list'),
	path('update-Raca/<int:pk>/', views.update_Raca.as_view(), name='raca_update'),
	path('delete-Raca/<int:pk>/', views.delete_Raca, name='raca_delete'),
]
