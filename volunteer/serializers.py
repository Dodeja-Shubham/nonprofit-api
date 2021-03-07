from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from .models import User

class UserSerializerForVolunteer(RegisterSerializer):
    title = serializers.CharField(max_length=5)
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=15)
    class Meta:
        model = User
        fields = ("title","name","email","phone","password1","password2")
    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        return email
    def validate_password1(self, password):
        return get_adapter().clean_password(password)
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                "The two password fields didn't match.")
        return data
    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'phone': self.validated_data.get('phone', ''),
            'title': self.validated_data.get('title', ''),
            'dob': self.validated_data.get('dob', ''),
            'location': self.validated_data.get('location', ''),
            'name': self.validated_data.get('name', ''),
            'occupation': self.validated_data.get('occupation', ''),
            'city': self.validated_data.get('city', ''),
        }
    def validate_phone(self, phone):
        return phone
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.phone = self.cleaned_data.get('phone')
        user.title = self.cleaned_data.get('title')
        user.dob = self.cleaned_data.get('dob')
        user.city = self.cleaned_data.get('city')
        user.name = self.cleaned_data.get('name')
        user.location = self.cleaned_data.get('location')
        user.occupation = self.cleaned_data.get('occupation')
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user