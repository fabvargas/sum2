from django.shortcuts import render
from .models import Country,  UserProfile, Sells,User, Product
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
   
    return render(request, 'home.html', )



def foro(request):
  
    return render(request, 'forowiki.html')

def dashboard(request):

    
    

    countries = Country.objects.all()
    profiles = UserProfile.objects.all()
    sells = Sells.objects.all()
    
    context = {
       
        'countries': countries,
        'profiles': profiles,
        'sells': sells,
    }
    
    
    return render(request, 'dashboard.html', context)


def shop(request):

    return render(request, 'shop.html')


@csrf_exempt
def comprar(request):
    if request.method == 'POST':
        try:
                data = json.loads(request.body)

                user_id = data.get('userId')
                version = data.get('version')
                precio = data.get('precio')
                
            

                if not all([user_id, version, precio]):
                    return JsonResponse({'success': False, 'error': 'Todos los campos son obligatorios.'}, status=400)

            
                try:
                    user = User.objects.get(pk=user_id)
                except User.DoesNotExist:
                    return JsonResponse({'success': False, 'error': 'Usuario no encontrado.'}, status=404)

                
                product, created = Product.objects.get_or_create(
                product_name=version,
                product_price=precio,
                )
                Sells.objects.create(user=user, product=product)
                return JsonResponse({'success': True, 'message': 'Compra registrada exitosamente.'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'JSON inválido.'}, status=400)

    return JsonResponse({'success': False, 'error': 'Método no permitido.'}, status=405)
