from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [

    path('cadastro/', views.createPet, name='create'),
    path('', views.paginacao, name='list'),
    path('update/<int:pk>/', views.updatePet.as_view(), name='update'),
    path('detail-pet/<int:pk>/', views.detailPet, name='detail'),
   

] 
