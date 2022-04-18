from django.test import TestCase
from .models import NeighbourHood
from django.contrib.auth.models import User
# Create your tests here.

user=User.objects.get(id=id)

class TestNeighbourhood(TestCase):
    def setUp(self):
        self.new_neighbourhood = NeighbourHood(name="test_neighbour", location="test_location", neighbourhood_photo='test.png', police_no=12345678, health_no=103030)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbourhood, NeighbourHood))

