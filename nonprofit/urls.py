# django imports
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Restframewok imports
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Reviewlin API",
        default_version='v1',
        description="This is the REST API documentation for Reviewlin API\'s",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
api_patterns = [
    path('volunteer/',include('volunteer.urls'), name='Volunteer APIs'),
    path('organization/',include('organization.urls'), name='organization APIs'),
    path('role/',include('role.urls'), name='role APIs'),
    path('application/',include('application.urls'), name='application APIs'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui')
]
