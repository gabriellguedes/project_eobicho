from django.urls import path
from . import views

app_name = 'unhas'

urlpatterns = [
	#Unhas
    path('add_unhas/', views.unhas_add, name='unhas_add'),
    path('list_unhas/', views.unhas_list, name='unhas_list'),
    path('update_unhas/<int:pk>/', views.unhas_update, name='unhas_update'),
    path('delete_unhas/<int:pk>/', views.unhas_delete, name='unhas_delete'), 
    
]
