from django.urls import path
from . import views 

app_name ='core'

urlpatterns =[
	path('', views.home, name='home' ),
	path('acesso_negado/', views.permission, name='permission'),
]