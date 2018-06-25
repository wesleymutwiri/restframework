from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient 
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.

class ModelTestCase(TestCase):
    '''
    Class that defines the test suite for the bucketlist models
    '''
    def setUp(self):
        '''
        define the test client and other test variables
        '''
        self.bucketlist_name = "Write world class code "
        self.bucketlist = Bucketlist(name = self.bucketlist_name)

    def test_create_model(self):
        '''
        Test the bucketlist model can create a bucketlist
        '''
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    '''
    Test suite for the api views 
    '''
    def SetUp(self):
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to the Himalayas'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")
    def test_api_can_create_a_bucketlist(self):
        '''
        Test the api has capability to create data
        '''
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)