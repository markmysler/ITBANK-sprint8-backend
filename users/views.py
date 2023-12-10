from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

class UserView(APIView):
      def get(self, request):
          token_key = request.auth.key
          user = Token.objects.get(key=token_key).user
          return Response({
              'username': user.username,
              'id': user.id,
          })