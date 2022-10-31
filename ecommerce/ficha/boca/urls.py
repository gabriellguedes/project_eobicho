from django.urls import path
from . import views

app_name = 'boca'

urlpatterns = [
	#Boca
    path('add_boca/', views.boca_add, name='boca_add'),
    path('list_boca/', views.boca_list, name='boca_list'),
    path('update_boca/<int:pk>/', views.boca_update, name='boca_update'),
    path('delete_boca/<int:pk>/', views.boca_delete, name='boca_delete'), 
    
]