from django.shortcuts import render
from rest_framework import generics 
from .serializer import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    '''
    This class defines the create behaviour of our rest api
    '''
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self,serializer):
        '''
        save the post data when creating a new bucketlist
        '''
        serializer.save()