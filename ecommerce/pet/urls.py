from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [
    
    path('list/', views.paginacao, name='list'),
    path('update/<int:pk>/', views.updatePet.as_view(), name='update'),
    path('detail-pet/<int:pk>/', views.detailPet, name='detail'),
    path('delete/<int:pk>/', views.deletePet.as_view(), name='delete'),
    path('cadastro/', views.createPet, name='create'),
    # Urls Fichas
    path('ficha/<int:pk>/', views.createFicha, name='createFicha'),
    path('fichas/', views.listFicha, name='listFicha'),
    path('oldficha/<int:pk>/<int:n>/', views.detailFicha, name='detailFicha'),
        
] 
