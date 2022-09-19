from django.urls import path
#from .views import form, listPet
from . import views

app_name = 'contas'

urlpatterns = [
    
    path('', views.home, name='home'),
    # Cliente 
    path('cliente_add/', views.cliente_add, name='cliente_add'),
    path('cliente_list/', views.cliente_list, name='cliente_list'),
    path('cliente_update/<int:pk>/', views.cliente_update.as_view(), name='cliente_update'),
    path('cliente_delete<int:pk>/', views.cliente_delete.as_view(), name='cliente_delete'),
        
] 
