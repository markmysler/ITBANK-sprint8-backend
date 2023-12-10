from rest_framework import serializers

from sucursales.models import Sucursal

class SucursalSerializer(serializers.ModelSerializer):
  class Meta:
      model = Sucursal
      fields = '__all__'