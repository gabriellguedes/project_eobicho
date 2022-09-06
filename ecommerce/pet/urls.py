from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [
    
    path('', views.form, name='form'),
    path('list/', views.paginacao, name='list'),
    path('update/<int:pk>/', views.updatePet.as_view(), name='update'),
    path('detail/<int:pk>/', views.detailPet, name='detail'),
    path('delete/<int:pk>/', views.deletePet.as_view(), name='delete'),
    path('anamnese/<int:pk>/', views.anamnese, name='anamnese'),
        
] 
