from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'pet'

urlpatterns = [

    path('cliente/add_pet/<int:pk>/', views.cliente_pet_add, name='cliente_pet_add'),
    path('add_pet/', views.pet_add, name='pet_add'), 
    path('list_pet/', views.paginacao, name='pet_list'),
    path('update_pet/<int:pk>/', views.pet_update, name='pet_update'),
    path('cliente/update_pet/<int:pk>/', views.cliente_pet_update, name='cliente_pet_update'),
    path('detail_pet/<int:pk>/', views.detailPet, name='pet_detail'),

    path('ajax/load-funcoes/', views.load_funcoes, name='ajax_load_funcoes'),

]


