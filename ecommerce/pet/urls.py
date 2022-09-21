from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [

    path('add-pet/', views.pet_add, name='pet_add'),
    path('list-pet/', views.paginacao, name='pet_list'),
    path('update-pet/<int:pk>/', views.pet_update, name='pet_update'),
    path('detail-pet/<int:pk>/', views.detailPet, name='pet_detail'),
   

] 
