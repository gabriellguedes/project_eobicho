from django.urls import path
from . import views
app_name= 'services'

urlpatterns = [
	path('New_Ficha/<int:pk>/', views.new_ficha, name='new_ficha'),
]
