from django.urls import path
# user imports
from . import views

urlpatterns = [
    path('all/', views.RoleView.as_view()),
    path('<int:id>/', views.RoleEachView.as_view()),
]
