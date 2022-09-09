from django.urls import path
from . import views

app_name = 'fichas'

urlpatterns = [
	# Urls Fichas
    path('ficha/<int:pk>/', views.createFicha, name='createFicha'),
    path('fichas/', views.listFicha, name='listFicha'),
    path('oldficha/<int:pk>/<int:n>/', views.detailFicha, name='detailFicha'),
]