from django.urls import path
from . import views
app_name= 'services'

urlpatterns = [
	path('banho_add/', views.banho_add, name='banho_add'),	
	path('banho_update/<int:pk>/', views.banho_update, name='banho_update'),
	path('banho_delete/<int:pk>/', views.banho_delete, name='banho_delete'),
	path('banho_list/', views.banho_list, name='banho_list'),

	path('tosa_add/', views.tosa_add, name='tosa_add'),	
	path('tosa_update/<int:pk>/', views.tosa_update, name='tosa_update'),
	path('tosa_delete/<int:pk>/', views.tosa_delete, name='tosa_delete'),
	path('tosa_list/', views.tosa_list, name='tosa_list'),

	path('itens_add/', views.itens_add, name='itens_add'),	
	path('itens_update/<int:pk>/', views.itens_update, name='itens_update'),
	path('itens_delete/<int:pk>/', views.itens_delete, name='itens_delete'),
	path('itens_list/', views.itens_list, name='itens_list'),

	path('New_Ficha/<int:pk>/', views.new_ficha, name='new_ficha'),
	path('add_ficha/', views.add_ficha, name='add_ficha'),
	path('detail_ficha/<int:pk>/', views.detail_ficha, name='detail_ficha'),
	path('detail_ficha_tutor/<int:pk>/', views.detail_ficha_tutor, name='detail_ficha_tutor'),
	path('banhoandtosa/', views.list_ficha, name='list_ficha'),
	path('delete_ficha/<int:pk>/', views.delete_ficha, name='delete_ficha'),
	path('permission_tutor/<int:pk>/', views.permission_tutor, name='permission_tutor'),
	path('atender_ficha/<int:pk>/', views.atender_ficha, name='atender_ficha'),
	path('finalizar_ficha/<int:pk>/', views.finalizar_ficha, name='finalizar_ficha'),
	path('permission_ficha_cancelada/<int:pk>/', views.permission_ficha_cancelada, name='permission_ficha_cancelada'),
]
