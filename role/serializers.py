from rest_framework import serializers
from .models import Role


class RoleSerializer(serializers.ModelSerializer):
    # Serializer for user model to store JSON Data
    class Meta:
        model = Role
        fields = '__all__'
