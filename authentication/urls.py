
from django.urls import path
from . import views

urlpatterns = [

    path('registrarse/', views.registrarse , name='registrarse'),
    path('inicio_sesion/', views.inicio_sesion , name='inicio_sesion'),
    path('mi_cuenta/', views.mi_cuenta , name='mi_cuenta'),
    path('recuperar_contrasena/', views.recuperar_contrasena , name='recuperar_contrasena'),

    path('registrar_usuario/', views.registrar_usuario , name='registrar_usuario'),
    path('login/', views.login , name='login'),
    path('pass_recovery/', views.pass_recovery , name='pass_recovery'),
    path('logout/', views.logout , name='logout'),
    
    path('reset_password/<uidb64>/', views.reset_password , name='restablecer_contrasena'),
    path('changepass/<uidb64>/', views.changepass , name='chamgepass'),
]

