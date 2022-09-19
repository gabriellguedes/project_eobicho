from django.urls import path
from . import views

app_name = 'sys'

urlpatterns = [
	# Dashboard
	path('', views.dashboard, name='sys_dashboard'),
	# Especies
	path('add-especie/', views.especie_add, name='especie_add'),
	path('addespecie/', views.add_Especie, name='add_Especie'),
	path('list-especie/', views.list_Especie, name='especie_list'),
	path('delete-especie/<int:pk>/', views.delete_Especie, name='especie_delete'),
	path('update-especie/<int:pk>/', views.update_Especie.as_view(), name='especie_update'),
	# Raças
	path('add-raca/', views.add_Raca, name='raca_add'),
	path('list-raca/', views.list_Raca, name='raca_list'),
	path('update-raca/<int:pk>/', views.update_Raca.as_view(), name='raca_update'),
	path('delete-raca/<int:pk>/', views.delete_Raca, name='raca_delete'),
]
