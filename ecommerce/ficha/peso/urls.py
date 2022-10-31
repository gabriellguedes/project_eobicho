from django.urls import path
from . import views

app_name = 'peso'
urlpatterns = [
	# Peso
    path('add_peso/<int:pk>/', views.peso_add, name='peso_add'),
    path('change_peso/<int:pk>/', views.peso_update, name='peso_update'),
]