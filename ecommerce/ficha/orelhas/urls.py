from django.urls import path
from . import views

app_name = 'orelhas'

urlpatterns = [
	#Orelhas
    path('add_orelhas/', views.orelhas_add, name='orelhas_add'),
    path('list_orelhas/', views.orelhas_list, name='orelhas_list'),
    path('update_orelhas/<int:pk>/', views.orelhas_update, name='orelhas_update'),
    path('delete_orelhas/<int:pk>/', views.orelhas_delete, name='orelhas_delete'), 
   
]