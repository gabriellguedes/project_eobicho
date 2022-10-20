from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'contas'

urlpatterns = [
    # Cliente 

    path('new_client/', views.new_client, name='new_user'),    
    path('new_user/', views.user_add, name='cliente_add'), 
    path('user_list/', views.user_list, name='cliente_list'),
    path('user_detail/<int:pk>/', views.user_detail, name='cliente_detail'),    
    path('user_detail_view/<int:pk>/', views.user_detail_admin, name='cliente_detail_admin'),
    path('user_update/<int:pk>/', views.user_update, name='cliente_update'),
    path('user_update_for_adm/<int:pk>/', views.user_update_for_adm, name='user_update_for_adm'),
    path('user_delete/<int:pk>/', views.user_delete.as_view(), name='cliente_delete'),
   
    path('', include('django.contrib.auth.urls')),  
] 
