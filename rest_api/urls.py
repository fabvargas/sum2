from django.urls import path
from . import views

urlpatterns = [
    path('sells/', views.sells_view, name='sells_list'),
    path('sells/<int:sell_id>/', views.sells_view, name='sells_detail'),

    path('usuario/', views.profile_view, name='perfil_list'),
    path('usuario/<int:user_id>/', views.profile_view, name='perfil_detail'),
]