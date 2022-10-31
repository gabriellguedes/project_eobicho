from django.urls import path
from . import views

app_name = 'especie'

urlpatterns = [
	# Especies
    path('add_especie/', views.especie_add, name='especie_add'),
    path('addespecie/', views.add_Especie, name='add_Especie'),
    path('list_especie/', views.list_Especie, name='especie_list'),
    path('delete_especie/<int:pk>/', views.delete_Especie, name='especie_delete'),
    path('update_especie/<int:pk>/', views.update_Especie, name='especie_update'),
    
]