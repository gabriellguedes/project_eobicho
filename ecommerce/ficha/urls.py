from django.urls import path
from . import views

app_name = 'fichas'

urlpatterns = [
	
    path('', views.listFicha, name='listFicha'),
    path('ficha/<int:pk>/', views.createFicha, name='createFicha'),
    path('oldficha/<int:pk>/<int:n>/', views.detailFicha, name='detailFicha'),
]