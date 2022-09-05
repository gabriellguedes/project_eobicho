from django.urls import path
#from .views import form, listPet
from . import views

app_name = 'accounts'

urlpatterns = [
    
    path('', views.home, name='home'),
  
        
] 
