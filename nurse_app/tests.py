from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
# Create your tests here.

class ModelTests(TestCase):
    def setUp(self):
     self.scrubs = Scrubs(
            name= "adidas",
            size = "L",
            color="Blue",
            description="testing",
            is_new = True,
            price=20,
        )
     
     self.scrubs.save()
    
    #checking whether the __str__ method of the scrubs model returns a string representation
    def test_model_rep(self):
        
     self.assertEqual(str(self.scrubs), "adidas")

    #verifying that the get_absolute_URL method returns a valid URL    
    def test_absolute_URL(self):
     print("In test_absolute_URL")
     print(f"self: {self}")
     expected_url = f'/scrub-detail/{self.scrubs.id}/'
     self.assertEqual(self.scrubs.get_absolute_url(), expected_url)
    #veyfying that default values are set correctly when an instance is created
    def test_defaults(self):
        default_scrub = Scrubs()
        self.assertFalse(default_scrub.is_new)
        self.assertEqual(default_scrub.price, 0)
