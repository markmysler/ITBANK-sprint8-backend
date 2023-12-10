from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cuenta, Tarjeta
from .serializers import TarjetaSerializer

class TarjetaListView(APIView):
   def get(self, request, customer_id):
       tarjeta = Tarjeta.objects.filter(customer_id=customer_id)
       if not tarjeta.exists():
           return Response([], status=status.HTTP_200_OK)
       serializer = TarjetaSerializer(tarjeta, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
