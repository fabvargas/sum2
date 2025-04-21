from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path( "shop", views.shop , name='shop'), 
    path('foro/', views.foro , name='foro'),
    path('dashboard/', views.dashboard , name='dashboard'),
    
    path('comprar/', views.comprar , name='comprar'),
    
    path('sells/eliminar/<int:sell_id>/', views.eliminar_sell, name='eliminar_sell'),
    path('sells/editar/<int:sell_id>/', views.editar_sell, name='editar_sell'),

    path('perfil/eliminar/<int:user_id>/', views.eliminar_perfil, name='eliminar_perfil'),
    path('perfil/editar/<int:user_id>/', views.editar_perfil, name='editar_perfil'),
    
]