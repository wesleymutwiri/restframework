from django.test import TestCase
from .models import Bucketlist
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
