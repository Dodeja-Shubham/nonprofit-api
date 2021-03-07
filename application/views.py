# Create your views here.
# Restframework Imports
from rest_framework import generics, mixins
from rest_framework.response import Response

# User Imports
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationView(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin):
    """Endpoint for list and Creation of Application
    """                       
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)
    
    def perform_create(self, serializer):
        serializer.save(volunteer=self.request.user)

class ApplicationEachView(generics.GenericAPIView,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin):
    '''
    Endpoint to View & Edit a single Application
    '''

    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
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