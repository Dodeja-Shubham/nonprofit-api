from django.shortcuts import render

# Create your views here.
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from rest_auth.views import LoginView, LogoutView
from .models import User
from .serializers import UserSerializerForVolunteer

class VolunteerRegistration(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializerForVolunteer
    queryset = User.objects.all()
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.save(request) # <---- INCLUDE REQUEST
                # return Response(serializer.data, status=status.HTTP_201_CREATED)
                if user:
                    token = Token.objects.create(user=user)
                    json = serializer.data
                    json["id"] = user.id
                    json['token'] = token.key
                    return Response(json, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            return Response({"message": "User Already Exits"})
        except Exception as e:
            return Response({"error":str(e)})

class VolunteerLogin(LoginView):
    """
    An endpoint for Login.
    """
    authentication_classes = []
    def get_response(self):
        try:
            user = self.request.user
            orginal_response = super().get_response()
            mydata = {"message": "User has logged in", 
            "status": "success",
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "dob": user.dob,
            }
            orginal_response.data.update(mydata)
            return orginal_response
        except Exception as e:
            return Response(str(e))

class VolunteerLogout(APIView):
    """
    An endpoint for Logout.
    """
    def post(self, request):
        try:
            user_obj = request.user
            logout(request)
            return Response({"success":"User Logged Out"})
        except Exception as e:
            return Response(str(e))