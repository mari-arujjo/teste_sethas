from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Consumidor
from .serializer import ConsumidorSerializer
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

@extend_schema(tags=['Consumidor'])
@api_view(['GET'])
def get_consumidores(request):
    consumidor = Consumidor.objects.all()
    serializer = ConsumidorSerializer(consumidor, many=True)
    return Response(serializer.data)

@extend_schema(
    tags=['Consumidor'],
    request=ConsumidorSerializer,
    responses={201:ConsumidorSerializer}
)
@api_view(['POST'])
def create_consumidores(request):
    serializer = ConsumidorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Consumidor'],
    request=ConsumidorSerializer,
    responses={201:ConsumidorSerializer}
)
@api_view(['PUT'])
def update_consumidores(request, pk:int):
    consumidor = get_object_or_404(Consumidor, pk=pk)
    serializer = ConsumidorSerializer(consumidor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(tags=['Consumidor'])
@api_view(['DELETE'])
def delete_consumidor(request, pk:int):
    consumidor = get_object_or_404(Consumidor, pk=pk)
    consumidor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)