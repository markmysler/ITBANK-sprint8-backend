from rest_framework import serializers
from django.contrib.auth.models import User
from clientes.models import Cliente
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['username', 'password']

class ClienteSerializer(serializers.ModelSerializer):
   user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

   class Meta:
       model = Cliente
       fields = ['user', 'customer_name', 'customer_surname', 'customer_dni', 'dob', 'customer_type']

   def create(self, validated_data):
      user = validated_data.pop('user')
      cliente = Cliente.objects.create(user=user, **validated_data)
      return cliente

class CustomRegisterSerializer(RegisterSerializer):
   def get_cleaned_data(self):
       data = super().get_cleaned_data()
       user_id = data.get('user').id if data.get('user') else None
       return {
           'username': data.get('username', ''),
           'user_id': user_id,
       }



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')