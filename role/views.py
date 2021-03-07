# Create your views here.
# Restframework Imports
from rest_framework import generics, mixins
from rest_framework.response import Response

# User Imports
from .models import Role
from .serializers import RoleSerializer

class RoleView(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin):
    """Endpoint for list and Creation of Role
    """                       
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

class RoleEachView(generics.GenericAPIView,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin):
    '''
    Endpoint to View & Edit a single Role
    '''

    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        '''
        GET Request
        '''
        if id:
            return self.retrieve(request)

    def put(self, request, id=None):
        '''
        Edit Request
        '''
        if id:
            return self.update(request, id)

    def patch(self, request, id=None):
        return self.partial_update(request, id)