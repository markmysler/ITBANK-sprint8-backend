from rest_framework.views import APIView
from rest_framework.response import Response
from clientes.models import Cliente

from cuentas.models import Cuenta
from .models import Prestamo
from .serializers import PrestamoSerializer, PrestamoSerializerPost
from django.utils import timezone

class PrestamoView(APIView):
   def get(self, request, customer_id):
       prestamos = Prestamo.objects.filter(customer_id=customer_id)
       serializer = PrestamoSerializer(prestamos, many=True)
       return Response(serializer.data)

   def post(self, request, customer_id):
       serializer = PrestamoSerializerPost(data=request.data)
       if serializer.is_valid():
           prestamo = serializer.save(customer_id=Cliente.objects.get(customer_id=customer_id), loan_date=timezone.now())
           target_account = Cuenta.objects.get(account_id=prestamo.target_account.account_id)
           new_balance = int(target_account.balance) + int(prestamo.loan_total)
           target_account.balance = new_balance
           target_account.save()
           return Response(serializer.data, status=201)
       return Response(serializer.errors, status=400)
