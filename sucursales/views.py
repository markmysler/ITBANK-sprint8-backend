from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from sucursales.models import Sucursal
from sucursales.serializers import SucursalSerializer

# Create your views here.

class SucursalListView(APIView):
    def get(self, request):
       sucursal = Sucursal.objects.all()
       if not sucursal.exists():
           return Response([], status=status.HTTP_200_OK)
       serializer = SucursalSerializer(sucursal, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)