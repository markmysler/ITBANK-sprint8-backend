


from rest_framework import generics

from clientes.models import Cliente
from .serializers import ClienteSerializer
from dj_rest_auth.registration.views import RegisterView
from django.contrib.auth import get_user_model


# Create your views here.

class ClienteView(generics.CreateAPIView):
 queryset = Cliente.objects.all()
 serializer_class = ClienteSerializer
 

User = get_user_model()

class CustomRegisterView(RegisterView):
 def get_response_data(self, user):
   data = super().get_response_data(user)
   if data is None:
       data = {}
   data['user_id'] = user.id
   return data