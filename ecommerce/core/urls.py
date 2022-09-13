from django.urls import path
from . import views 

app_name ='core'

urlpatterns =[
	path('login/', views.login, name='login' ),
	# Especies
	path('addespecie/', views.add_Especie, name='add_Especie'),
	path('listEspecie/', views.list_Especie, name='list_Especie'),
	path('delete-Especie/<int:pk>/', views.delete_Especie, name='del_Especie'),
	# Raças
	path('addraca/', views.add_Raca, name='add_Raca'),
]