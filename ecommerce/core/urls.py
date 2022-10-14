from django.urls import path
from . import views 

app_name ='core'

urlpatterns =[
	path('', views.login, name='home' ),
	path('photo_user', views.photo_user, name='photo_user'),
	
]