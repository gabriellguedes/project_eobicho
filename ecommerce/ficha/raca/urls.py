from django.urls import path
from . import views

app_name = 'raca'

urlpatterns = [
	# Raças
    path('add_raca/', views.add_Raca, name='raca_add'),
    path('list_raca/', views.list_Raca, name='raca_list'),
    path('update_raca/<int:pk>/', views.update_Raca, name='raca_update'),
    path('delete_raca/<int:pk>/', views.delete_Raca, name='raca_delete'),

]