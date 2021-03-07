from django.urls import path
from volunteer import views

urlpatterns = [
    path('register/', views.VolunteerRegistration.as_view(), name="register"),
    path('login/', views.VolunteerLogin.as_view(), name="login"),
    path('logout/', views.VolunteerLogout.as_view(), name="logout"),
]
