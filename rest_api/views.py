from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import UserProfile, Sells
from .serializers import UserProfileSerializer, SellSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET'])
def profile_view(request, user_id=None):
    if user_id is not None:
        try:
            profile = UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            return Response(
                {"error": f"No se encontró un perfil con user_id = {user_id}"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    else:
        profiles = UserProfile.objects.all()
        if not profiles:
            return Response(
                {"error": "No hay perfiles disponibles"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def sells_view(request, sell_id=None):
    if request.method == 'GET':
        if sell_id is not None:
            try:
                sell = Sells.objects.get(sells_id=sell_id)
            except Sells.DoesNotExist:
                return Response(
                    {"error": f"No se encontró una venta con sells_id = {sell_id}"},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = SellSerializer(sell)
            return Response(serializer.data)
        else:
            sells = Sells.objects.all()
            if not sells:
                return Response(
                    {"error": "No hay ventas registradas"},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = SellSerializer(sells, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT' and sell_id is not None:
        try:
            sell = Sells.objects.get(sells_id=sell_id)
        except Sells.DoesNotExist:
            return Response(
                {"error": f"No se puede actualizar: venta con sells_id = {sell_id} no existe"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = SellSerializer(sell, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' and sell_id is not None:
        try:
            sell = Sells.objects.get(sells_id=sell_id)
        except Sells.DoesNotExist:
            return Response(
                {"error": f"No se puede eliminar: venta con sells_id = {sell_id} no existe"},
                status=status.HTTP_404_NOT_FOUND
            )
        sell.delete()
        return Response({"message": "Venta eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)

    return Response(
        {"error": "Método no permitido o sell_id requerido"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED
    )
