from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    # Serializer for user model to store JSON Data
    class Meta:
        model = Application
        fields = '__all__'
