from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [

    path('cadastro/', views.pet_add, name='pet_add'),
    path('', views.paginacao, name='pet_list'),
    path('update/<int:pk>/', views.updatePet.as_view(), name='pet_update'),
    path('detail-pet/<int:pk>/', views.detailPet, name='pet_detail'),
   

] 
