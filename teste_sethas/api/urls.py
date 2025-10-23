from django.urls import path
from .views import get_consumidores, create_consumidores, update_consumidores, delete_consumidor

urlpatterns = [
    path('clientes/', get_consumidores, name="get_consumidores"),
    path('clientes/create', create_consumidores, name="create_consumidores"),
    path('clientes/update/<int:pk>', update_consumidores, name="update_consumidores"),
    path('clientes/delete/<int:pk>', delete_consumidor, name="delete_consumidor")
]