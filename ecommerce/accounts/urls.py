from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'contas'

urlpatterns = [
    # Cliente 

    path('new_user/', views.user_new, name='new_user'),    
    path('accounts/register/', views.cliente_add, name='cliente_add'), 
    path('cliente_list/', views.cliente_list, name='cliente_list'),
    path('cliente_detail/<int:pk>/', views.cliente_detail, name='cliente_detail'),    
    path('cliente_detail_view/<int:pk>/', views.cliente_detail_admin, name='cliente_detail_admin'),
    path('cliente_update/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('cliente_delete/<int:pk>/', views.cliente_delete.as_view(), name='cliente_delete'),
   
    path('', include('django.contrib.auth.urls')),  
] 
