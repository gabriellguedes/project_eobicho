from django.urls import path
from . import views

app_name = 'olhos'

urlpatterns = [
	#Olhos
    path('add_olhos/', views.olhos_add, name='olhos_add'),
    path('list_olhos/', views.olhos_list, name='olhos_list'),
    path('update_olhos/<int:pk>/', views.olhos_update, name='olhos_update'),
    path('delete_olhos/<int:pk>/', views.olhos_delete, name='olhos_delete'), 
    
]