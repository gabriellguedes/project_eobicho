from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'pet'

urlpatterns = [

    path('cliente_add_pet/<int:pk>/', views.cliente_pet_add, name='cliente_pet_add'),
    path('add_pet/', views.pet_add, name='pet_add'), 
    path('list_pet/', views.paginacao, name='pet_list'),
    path('update_pet/<int:pk>/', views.pet_update, name='pet_update'),
    path('detail_pet/<int:pk>/', views.detailPet, name='pet_detail'),
    # Peso
    path('add_peso/<int:pk>/', views.peso_add, name='peso_add'),
    path('change_peso/<int:pk>/', views.peso_update, name='peso_update'),
    # Especies
    path('add_especie/', views.especie_add, name='especie_add'),
    path('addespecie/', views.add_Especie, name='add_Especie'),
    path('list_especie/', views.list_Especie, name='especie_list'),
    path('delete_especie/<int:pk>/', views.delete_Especie, name='especie_delete'),
    path('update_especie/<int:pk>/', views.update_Especie, name='especie_update'),
    # Raças
    path('add_raca/', views.add_Raca, name='raca_add'),
    path('list_raca/', views.list_Raca, name='raca_list'),
    path('update_raca/<int:pk>/', views.update_Raca, name='raca_update'),
    path('delete_raca/<int:pk>/', views.delete_Raca, name='raca_delete'),

    path('ajax/load-funcoes/', views.load_funcoes, name='ajax_load_funcoes'),
    path('ajax/load-cliente/', views.load_cliente, name='ajax_load_cliente'),
    path('ajax/update-pet/', views.load_update_pet, name='ajax_update_pet'),
]


