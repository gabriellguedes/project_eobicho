from django.urls import path
from . import views

app_name = 'fichas'

urlpatterns = [
	
    # Prontuário
    path('list-ficha/', views.prontuario_list, name='ficha_list'),
    path('add_ficha/<int:pk>/', views.prontuario_create, name='ficha_add'),
    path('oldficha/<int:pk>/<int:n>/', views.prontuario_detail, name='ficha_detail'),
    
    # Pele
    path('add_tipo_pele/', views.pele_add, name='pele_add'),
    path('list_peles/', views.pele_list, name='pele_list'),
    path('pele_update/<int:pk>/', views.pele_update, name='pele_update'),
    path('pele_delete/<int:pk>/', views.pele_delete, name='pele_delete'),

    #Doenças
    path('add_doenca/', views.doenca_add, name='doenca_add'),
    path('list_doenca/', views.doenca_list, name='doenca_list'),
    path('update_doenca/<int:pk>/', views.doenca_update, name='doenca_update'),
    path('delete_doenca/<int:pk>/', views.doenca_delete, name='doenca_delete'),
]