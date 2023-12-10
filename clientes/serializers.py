from django.contrib.auth.models import User
from rest_framework import serializers

from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields="__all__"
        read_only_fields = (
            "customer_id",
        )
    owner= serializers.ReadOnlyField(source='owner.username')
class UserSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(many=True, queryset=Cliente.objects.all())
    class Meta:
        model = User
        fields = ["id", "username", "cliente"]