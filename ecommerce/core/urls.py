from django.urls import path
from . import views 

app_name ='core'

urlpatterns =[
	path('', views.login, name='login' ),
	# Especies
	path('add-especie/', views.especie_add, name='especie_add'),
	path('addespecie/', views.add_Especie, name='add_Especie'),
	path('listEspecie/', views.list_Especie, name='list_Especie'),
	path('delete-Especie/<int:pk>/', views.delete_Especie, name='del_Especie'),
	path('update-Especie/<int:pk>/', views.update_Especie.as_view(), name='update_Especie'),
	# Raças
	path('add-raca/', views.add_Raca, name='add_Raca'),
	path('list-Raca/', views.list_Raca, name='list_Raca'),
	path('update-Raca/<int:pk>/', views.update_Raca, name='update_Raca'),
	path('delete-Raca/<int:pk>/', views.delete_Raca, name='delete_Raca'),
]