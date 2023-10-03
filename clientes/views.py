from django.shortcuts import render
from clientes.serializer import ClienteSerializer
from clientes.models import Cliente
from rest_framework import viewsets, generics

# Create your views here.
class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer