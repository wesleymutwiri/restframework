from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient 
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your tests here.

class ModelTestCase(TestCase):
    '''
    Class that defines the test suite for the bucketlist models
    '''
    def setUp(self):
        '''
        define the test client and other test variables
        '''
        user = User.objects.create(username="nerd")

        self.name = "Write world class code "
        self.bucketlist = Bucketlist(name = self.name, owner=user)

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
        '''
        Define the test client and other test variables
        '''
        user = User.objects.create(username="nerd")

        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.bucketlist_data = {'name': 'Go to the Himalayas'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        '''
        Test the api has capability to create data
        '''
        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_bucketlist(self):
        '''
        Test the api can get a given bucketlist
        '''
        bucketlist = Bucketlist.objects.get(id=1)
        response = self.client.get(
            '/bucketlists/',
            reverse('details', kwargs={'pk': bucketlist.id}),format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        '''
        Test if the api can update a given bucketlist
        '''
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name':'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_can_delete_bucketlist(self):
        '''
        Test the api can delete a bucketlist
        '''
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json', 
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)