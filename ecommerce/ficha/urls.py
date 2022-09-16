from django.urls import path
from . import views

app_name = 'fichas'

urlpatterns = [
	
    path('list-ficha/', views.listFicha, name='ficha_list'),
    path('add_ficha/<int:pk>/', views.createFicha, name='ficha_add'),
    path('oldficha/<int:pk>/<int:n>/', views.detailFicha, name='ficha_detail'),
]