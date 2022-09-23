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

    #ectoparasitas
    path('add_ectoparasitas/', views.ectoparasitas_add, name='ectoparasitas_add'),
    path('list_ectoparasitas/', views.ectoparasitas_list, name='ectoparasitas_list'),
    path('update_ectoparasitas/<int:pk>/', views.ectoparasitas_update, name='ectoparasitas_update'),
    path('delete_ectoparasitas/<int:pk>/', views.ectoparasitas_delete, name='ectoparasitas_delete'),

    #infec_pele
    path('add_infec_pele/', views.infec_pele_add, name='infec_pele_add'),
    path('list_infec_pele/', views.infec_pele_list, name='infec_pele_list'),
    path('update_infec_pele/<int:pk>/', views.infec_pele_update, name='infec_pele_update'),
    path('delete_infec_pele/<int:pk>/', views.infec_pele_delete, name='infec_pele_delete'),

    # Pelos
    path('add_tipo_pelos/', views.pelos_add, name='pelos_add'),
    path('list_pelos/', views.pelos_list, name='pelos_list'),
    path('update_pelos/<int:pk>/', views.pelos_update, name='pelos_update'),
    path('delete_pelos/<int:pk>/', views.pelos_delete, name='pelos_delete'),

    # Estado Pelos
    path('add_estado_pelos/', views.estado_pelos_add, name='estado_pelos_add'),
    path('list_estado_pelos/', views.estado_pelos_list, name='estado_pelos_list'),
    path('update_estado_pelos/<int:pk>/', views.estado_pelos_update, name='estado_pelos_update'),
    path('delete_estado_pelos/<int:pk>/', views.estado_pelos_delete, name='estado_pelos_delete'),

     # Condição dos Pelos
    path('add_condicao_pelos/', views.condicao_pelos_add, name='condicao_pelos_add'),
    path('list_condicao_pelos/', views.condicao_pelos_list, name='condicao_pelos_list'),
    path('update_condicao_pelos/<int:pk>/', views.condicao_pelos_update, name='condicao_pelos_update'),
    path('delete_condicao_pelos/<int:pk>/', views.condicao_pelos_delete, name='condicao_pelos_delete'),

]