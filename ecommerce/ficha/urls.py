from django.urls import path
from . import views

app_name = 'fichas'

urlpatterns = [
	
    path('list-ficha/', views.prontuario_list, name='ficha_list'),
    path('add_ficha/<int:pk>/', views.prontuario_create, name='ficha_add'),
    path('oldficha/<int:pk>/<int:n>/', views.prontuario_detail, name='ficha_detail'),
]