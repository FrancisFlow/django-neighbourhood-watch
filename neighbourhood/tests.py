from django.test import TestCase
from .models import NeighbourHood, Business
from django.contrib.auth.models import User
# Create your tests here.

user=User.objects.get(id=id)

class TestNeighbourhood(TestCase):
    def setUp(self):
        self.new_neighbourhood = NeighbourHood(name="test_neighbour", location="test_location", neighbourhood_photo='test.png', police_no=12345678, health_no=103030)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbourhood, NeighbourHood))

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='Test Business')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_method(self):
        self.business.save()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.business.save()
        self.business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)