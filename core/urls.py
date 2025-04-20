from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path( "shop", views.shop , name='shop'), 
    path('foro/', views.foro , name='foro'),
    path('dashboard/', views.dashboard , name='dashboard'),
    
    path('comprar/', views.comprar , name='comprar'),
    
]