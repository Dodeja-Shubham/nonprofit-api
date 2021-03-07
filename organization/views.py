# Restframework Imports
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

# User Imports
from .models import Organization
from .serializers import OrganizationSerializer

class OrganizationView(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin):
    """Endpoint for list and Creation of Organization
    """                       
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

class OrganizationEachView(generics.GenericAPIView,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin):
    '''
    Endpoint to View & Edit a single Organization
    '''

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
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