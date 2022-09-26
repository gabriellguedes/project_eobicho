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


    #Boca
    path('add_boca/', views.boca_add, name='boca_add'),
    path('list_boca/', views.boca_list, name='boca_list'),
    path('update_boca/<int:pk>/', views.boca_update, name='boca_update'),
    path('delete_boca/<int:pk>/', views.boca_delete, name='boca_delete'), 
    
    #Unhas
    path('add_unhas/', views.unhas_add, name='unhas_add'),
    path('list_unhas/', views.unhas_list, name='unhas_list'),
    path('update_unhas/<int:pk>/', views.unhas_update, name='unhas_update'),
    path('delete_unhas/<int:pk>/', views.unhas_delete, name='unhas_delete'), 
    
    #Olhos
    path('add_olhos/', views.olhos_add, name='olhos_add'),
    path('list_olhos/', views.olhos_list, name='olhos_list'),
    path('update_olhos/<int:pk>/', views.olhos_update, name='olhos_update'),
    path('delete_olhos/<int:pk>/', views.olhos_delete, name='olhos_delete'), 
    
    #Orelhas
    path('add_orelhas/', views.orelhas_add, name='orelhas_add'),
    path('list_orelhas/', views.orelhas_list, name='orelhas_list'),
    path('update_orelhas/<int:pk>/', views.orelhas_update, name='orelhas_update'),
    path('delete_orelhas/<int:pk>/', views.orelhas_delete, name='orelhas_delete'), 
    
    #Patas
    path('add_patas/', views.patas_add, name='patas_add'),
    path('list_patas/', views.patas_list, name='patas_list'),
    path('update_patas/<int:pk>/', views.patas_update, name='patas_update'),
    path('delete_patas/<int:pk>/', views.patas_delete, name='patas_delete'),

]