from django.urls import path
from . import views

app_name = 'doenca'

urlpatterns = [
	#Doenças
    path('add_doenca/', views.doenca_add, name='doenca_add'),
    path('list_doenca/', views.doenca_list, name='doenca_list'),
    path('update_doenca/<int:pk>/', views.doenca_update, name='doenca_update'),
    path('delete_doenca/<int:pk>/', views.doenca_delete, name='doenca_delete'),
    
]