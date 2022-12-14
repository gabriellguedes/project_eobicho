from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'fichas'

urlpatterns = [
	
    # Prontuário
    path('list_anamneses/', views.prontuario_list, name='ficha_list'),
    path('add_ficha_anamnese/<int:pk>/', views.prontuario_create, name='ficha_add'),
    path('oldficha_anamnese/<int:pk>/<int:n>/', views.prontuario_detail, name='ficha_detail'),
    path('teste/', views.add_test, name='test_ficha'),

    #Includes
    path('boca/', include('ecommerce.ficha.boca.urls')),
    path('doenca', include('ecommerce.ficha.doenca.urls')),
    path('especie/', include('ecommerce.ficha.especie.urls')),    
    path('olhos/', include('ecommerce.ficha.olhos.urls')),    
    path('orelhas/', include('ecommerce.ficha.orelhas.urls')),    
    path('patas/', include('ecommerce.ficha.patas.urls')),
    path('pele/', include('ecommerce.ficha.pele.urls')),
    path('pelos/', include('ecommerce.ficha.pelos.urls')),
    path('peso/', include('ecommerce.ficha.peso.urls')),
    path('temperamento/', include('ecommerce.ficha.temperamento.urls')),
    path('raca/', include('ecommerce.ficha.raca.urls')),
    path('unhas/', include('ecommerce.ficha.unhas.urls')),  
]
