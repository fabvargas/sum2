from django.shortcuts import render

import json
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from core.models import User,UserType,Country, UserProfile
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from django.utils.http import urlsafe_base64_decode


# Create your views here.


def registrarse(request):

    return render(request, 'registrase_wiki.html')

def inicio_sesion(request):

    return render(request, 'inicio_sesion_wiki.html')

def mi_cuenta(request):

    return render(request, 'micuentatf.html')

def recuperar_contrasena(request):
  
    
    return render(request, 'recuperarcontra.html')

def reset_password(request, uidb64):
    return render(request, 'reset_password.html', {'uidb64': uidb64})




@csrf_exempt  # Solo para pruebas. Usa CSRF en producción
def registrar_usuario(request):
    print(request.body)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            password = data.get('contrasena')
            nombre = data.get('nombre')
            telefono = data.get('telefono')
            pais = data.get('pais')
            permisos = data.get('permisos')  # "user" o "admin"
            
            print(email, password, nombre, telefono, pais, permisos)

            if not all([email, password, nombre, telefono,  pais, permisos]):
                return JsonResponse({'status': 'error', 'message': 'Todos los campos son obligatorios.'}, status=400)


            if User.objects.filter(user_email=email).exists():
                return JsonResponse({'status': 'error', 'message': 'Este correo ya está registrado.'}, status=400)
            
            user_type, _ = UserType.objects.get_or_create(user_type_name=permisos)
            
            country, _ = Country.objects.get_or_create(country_name=pais)
            
            

            hashed_password = make_password(password)
            user = User(user_email=email, user_password=hashed_password, user_type=user_type)
            user.save()
            
            user_profile = UserProfile(
                user=user,
                user_name=nombre,
                user_phone=telefono,
                user_country=country,
              
            )
            user_profile.save()


            return JsonResponse({'status': 'success', 'message': 'Usuario registrado correctamente.'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Datos JSON inválidos.'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@csrf_exempt  # Para pruebas. En producción, protege con CSRF
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            password = data.get('contrasena')
            
          

            if not email or not password:
                return JsonResponse({'success': False, 'error': 'Todos los campos son obligatorios.'}, status=400)

            user = User.objects.filter(user_email=email).first()
            profile = UserProfile.objects.filter(user_id=user.user_id).first()
            

            if user and check_password(password, user.user_password):
                
                request.session['user_id'] = user.user_id 
                request.session['user_email'] = user.user_email
                request.session['user_type'] = user.user_type.user_type_name
                request.session['user_name'] = profile.user_name
                request.session['user_phone'] = profile.user_phone
                request.session['user_country'] = profile.user_country.country_name
                
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Credenciales incorrectas.'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Datos JSON inválidos.'}, status=400)

    return JsonResponse({'success': False, 'error': 'Método no permitido.'}, status=405)

@csrf_exempt
def pass_recovery(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            if not email:
                return JsonResponse({'success': False, 'error': 'Email es requerido.'}, status=400)

            try:
                user = User.objects.get(user_email=email)
            except User.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Usuario no encontrado con ese email.'}, status=404)
            
                  
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

            reset_link = f'http://127.0.0.1:8000/auth/reset_password/{uidb64}'

          
            send_mail(
                'Recuperación de contraseña',
                f'Hola {user.user_email},\n\nPara restablecer tu contraseña, haz clic en el siguiente enlace:\n\n{reset_link}\n\n'
                'Si no solicitaste este correo, puedes ignorarlo.',
                'noreply@tusitio.com',
                [email],
                fail_silently=False,
            )

            return JsonResponse({'success': True, 'message': 'Correo de recuperación enviado.'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Método no permitido.'}, status=405)

@csrf_exempt
def changepass(request, uidb64):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            user_id = urlsafe_base64_decode(uidb64).decode('utf-8')
      
            new_password = data.get('contrasena')

            if  not new_password:
                return JsonResponse({'success': False, 'error': 'Todos los campos son obligatorios.'}, status=400)

            user = User.objects.get(user_id=user_id)
            
            if user:
                hashed_password = make_password(new_password)
                user.user_password = hashed_password
                user.save()
                return JsonResponse({'success': True, 'message': 'Contraseña actualizada correctamente.'})
            else:
                return JsonResponse({'success': False, 'error': 'Usuario no encontrado.'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Datos JSON inválidos.'}, status=400)

    return JsonResponse({'success': False, 'error': 'Método no permitido.'}, status=405)


def logout(request):
    request.session.flush()
    return redirect('home')