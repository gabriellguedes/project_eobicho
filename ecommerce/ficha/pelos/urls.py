from django.urls import path
from . import views

app_name = 'pelos'

urlpatterns = [
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
    # PELAGEM
    path('add_pelagem/', views.pelagem_add, name='pelagem_add'),
    path('list_pelagens/', views.pelagem_list, name='pelagem_list'),
    path('update_pelagem/<int:pk>/', views.pelagem_update, name='pelagem_update'),
    path('delete_pelagem/<int:pk>/', views.pelagem_delete, name='pelagem_delete'),
    #Colorações
    path('add_coloracao/', views.coloracao_add, name='coloracao_add'),
    path('list_coloracoes/', views.coloracao_list, name='coloracao_list'),
    path('update_coloracao/<int:pk>/', views.coloracao_update, name='coloracao_update'),
    path('delete_coloracao/<int:pk>/', views.coloracao_delete, name='coloracao_delete'),
]