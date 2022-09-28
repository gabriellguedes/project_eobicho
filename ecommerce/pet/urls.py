from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [

    path('cliente_add_pet/<int:pk>/', views.cliente_pet_add, name='cliente_pet_add'),
    path('add_pet/', views.pet_add, name='pet_add'),
    path('list_pet/', views.paginacao, name='pet_list'),
    path('update_pet/<int:pk>/', views.pet_update, name='pet_update'),
    path('detail_pet/<int:pk>/', views.detailPet, name='pet_detail'),
    # Especies
    path('adde_specie/', views.especie_add, name='especie_add'),
    path('addespecie/', views.add_Especie, name='add_Especie'),
    path('list_especie/', views.list_Especie, name='especie_list'),
    path('delete_especie/<int:pk>/', views.delete_Especie, name='especie_delete'),
    path('update_especie/<int:pk>/', views.update_Especie.as_view(), name='especie_update'),
    # Raças
    path('add_raca/', views.add_Raca, name='raca_add'),
    path('list_raca/', views.list_Raca, name='raca_list'),
    path('update_raca/<int:pk>/', views.update_Raca.as_view(), name='raca_update'),
    path('delete_raca/<int:pk>/', views.delete_Raca, name='raca_delete'),
   

] 
