from django.urls import path
# user imports
from . import views

urlpatterns = [
    path('all/', views.ApplicationView.as_view()),
    path('<int:id>/', views.ApplicationEachView.as_view()),
]
