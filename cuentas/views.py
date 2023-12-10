from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cuenta
from .serializers import CuentaSerializer

class CuentaListView(APIView):
   def get(self, request, customer_id):
       cuenta = Cuenta.objects.filter(customer_id=customer_id)
       if not cuenta.exists():
           return Response([], status=status.HTTP_200_OK)
       serializer = CuentaSerializer(cuenta, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
