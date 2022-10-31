from django.urls import path
from . import views

app_name = 'patas'

urlpatterns = [
	 #Patas
    path('add_patas/', views.patas_add, name='patas_add'),
    path('list_patas/', views.patas_list, name='patas_list'),
    path('update_patas/<int:pk>/', views.patas_update, name='patas_update'),
    path('delete_patas/<int:pk>/', views.patas_delete, name='patas_delete'),
    
]