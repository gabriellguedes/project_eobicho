from django.urls import path
from . import views

app_name = 'pele'

urlpatterns = [
	# Pele
    path('add_tipo_pele/', views.pele_add, name='pele_add'),
    path('list_peles/', views.pele_list, name='pele_list'),
    path('pele_update/<int:pk>/', views.pele_update, name='pele_update'),
    path('pele_delete/<int:pk>/', views.pele_delete, name='pele_delete'),
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
    
]