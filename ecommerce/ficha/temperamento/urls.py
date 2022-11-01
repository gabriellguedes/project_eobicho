from django.urls import path
from . import views

app_name = 'temperamento'

urlpatterns = [
	# Raças
    path('add_temperamento/', views.temperamento_add, name='temperamento_add'),
    path('list_temperamento/', views.temperamento_list, name='temperamento_list'),
    path('update_temperamento/<int:pk>/', views.temperamento_update, name='temperamento_update'),
    path('delete_temperamento/<int:pk>/', views.temperamento_delete, name='temperamento_delete'),

]