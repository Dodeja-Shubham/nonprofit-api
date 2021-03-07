from django.urls import path
# user imports
from . import views

urlpatterns = [
    path('all/', views.OrganizationView.as_view()),
    path('<int:id>/', views.OrganizationEachView.as_view()),
]
