from django.shortcuts import render, redirect, get_object_or_404
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



    # Eliminar venta
def eliminar_sell(request, sell_id):
    sell = get_object_or_404(Sells, pk=sell_id)
    sell.delete()
    return redirect('dashboard')  # Asegúrate de tener esta vista o cambia el destino

# Editar venta
def editar_sell(request, sell_id):
    sell = get_object_or_404(Sells, pk=sell_id)
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        try:
            product = Product.objects.get(pk=product_id)
            sell.product = product
            sell.save()
            return redirect('dashboard')
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)

    return render(request, 'editar_sell.html', {'sell': sell, 'products': products})


# Eliminar perfil
def eliminar_perfil(request, user_id):
    profile = get_object_or_404(UserProfile, pk=user_id)
    user = get_object_or_404(User, pk=user_id)
    profile.delete()
    user.delete()
    return redirect('dashboard')

# Editar perfil
@csrf_exempt
def editar_perfil(request, user_id):
    profile = get_object_or_404(UserProfile, pk=user_id)
    country_name = get_object_or_404(Country, pk=profile.user_country_id)
    
    if request.method == 'POST':
        
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone')
        country = data.get('country')
        
        
        country, _ = Country.objects.get_or_create(country_name=country)
        
        if not all ([name, phone, country]):
            return JsonResponse({'success': False, 'error': 'Todos los campos son obligatorios.'}, status=400)
        try:
            profile.user_name = name
            profile.user_phone = phone
            profile.user_country = country
            profile.save()
            
            return JsonResponse({'success': True, 'message': 'Perfil actualizado exitosamente.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
   
    return render(request, 'editar_perfil.html', {
        'profile': profile,
        'countries': country_name
    })
   
