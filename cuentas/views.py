import random
from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from clientes.models import Cliente
from .models import Cuenta
from .serializers import CuentaSerializer, CuentaSerializerForPost

class CuentaListView(APIView):
    def get(self, request, customer_id):
       cuenta = Cuenta.objects.filter(customer_id=customer_id)
       if not cuenta.exists():
           return Response([], status=status.HTTP_200_OK)
       serializer = CuentaSerializer(cuenta, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, customer_id):
       serializer = CuentaSerializerForPost(data=request.data)
       if serializer.is_valid():
           serializer.save(
               customer_id=Cliente.objects.get(customer_id =customer_id),
               balance=0,
               iban=''.join(random.choices('0123456789', k=10))
           )
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)