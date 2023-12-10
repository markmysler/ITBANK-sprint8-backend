from rest_framework import serializers
from .models import Cuenta

class CuentaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Cuenta
       fields = ['account_id', 'customer_id', 'balance', 'iban', 'account_type']

class CuentaSerializerForPost(serializers.ModelSerializer):
  class Meta:
      model = Cuenta
      fields = ['account_type']