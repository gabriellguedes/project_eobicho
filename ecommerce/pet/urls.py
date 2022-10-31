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

    path('ajax/load-funcoes/', views.load_funcoes, name='ajax_load_funcoes'),
    path('ajax/load-cliente/', views.load_cliente, name='ajax_load_cliente'),
    path('ajax/update-pet/', views.load_update_pet, name='ajax_update_pet'),

]


