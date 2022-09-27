from django.urls import path
#from .views import form, listPet
from . import views

app_name = 'contas'

urlpatterns = [
    
    path('', views.home, name='home'),

    # Cliente 
    path('cliente_add/', views.cliente_add, name='cliente_add'),
    path('cliente_list/', views.cliente_list, name='cliente_list'),
    path('cliente_detail/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente_update/<int:pk>/', views.cliente_update.as_view(), name='cliente_update'),
    path('cliente_delete<int:pk>/', views.cliente_delete.as_view(), name='cliente_delete'),
    # Funcionários
    path('funcionario_add/', views.funcionario_add, name='funcionario_add'),
    path('funcionario_list/', views.funcionario_list, name= 'funcionario_list'),
    path('funcionario_update/<int:pk>/', views.funcionario_update, name='funcionario_update'),
    path('funcionario_delete/<int:pk>/', views.funcionario_delete.as_view(), name='funcionario_delete'),
   
        
] 
