from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from clientes.models import Cliente
from .models import Cuenta, Tarjeta
from .serializers import TarjetaSerializer
from django.utils import timezone
import random

class TarjetaListView(APIView):
    def get(self, request, customer_id):
        tarjeta = Tarjeta.objects.filter(customer_id__pk=customer_id)
        if not tarjeta.exists():
            return Response([], status=status.HTTP_200_OK)
        serializer = TarjetaSerializer(tarjeta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def post(self, request, customer_id):
      serializer = TarjetaSerializer(data=request.data)
      if serializer.is_valid():
          card_type = serializer.validated_data.get('card_type')
          card_issuer = serializer.validated_data.get('card_issuer')
          related_account = serializer.validated_data.get('related_account')
          if card_type == 'DEBITO' and not related_account:
              return Response({'error': 'related_account is required for debit cards'}, status=status.HTTP_400_BAD_REQUEST)
          cvv = random.randint(100, 999) # Generate a random 3-digit number
          emision_date = timezone.now().date() # Today's date
          expiry_date = emision_date + timezone.timedelta(days=5*365) # 5 years in the future
          tarjeta = Tarjeta.objects.create(
              cvv=cvv,
              emision_date=emision_date,
              expiry_date=expiry_date,
              card_type=card_type,
              card_issuer=card_issuer,
              customer_id=Cliente.objects.get(customer_id = customer_id),
              related_account=related_account if card_type == 'DEBITO' else None,
          )
          serializer = TarjetaSerializer(tarjeta)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
