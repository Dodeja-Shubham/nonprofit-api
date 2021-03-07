from rest_framework import serializers
from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    # Serializer for user model to store JSON Data
    class Meta:
        model = Organization
        fields = '__all__'
