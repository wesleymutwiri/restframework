from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    '''
    This class defines the create behaviour of our rest api
    '''
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self,serializer):
        '''
        save the post data when creating a new bucketlist
        '''
        serializer.save(owner=self.request.user)
        
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    '''
    This class handles the http GET, PUT and DELETE requests.
    '''
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
