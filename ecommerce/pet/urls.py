from django.urls import path
#from .views import form, listPet
from . import views

app_name = 'pet'

urlpatterns = [
    path('', views.paginacao, name='list'),
    path('newpet', views.form, name='form'),
    path('update/<int:pk>/', views.updatePet.as_view(), name='update'),
    path('detail/<int:pk>/', views.detailPet, name='detail'),
    path('delete/<int:pk>/', views.deletePet.as_view(), name='delete'),
    path('formInspecaoPet/', views.FormInspecaoPet, name='InspecaoPet'),
        
] 
