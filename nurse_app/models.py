# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.

class Scrubs(models.Model):

    #List of choices for colors value in database, human readable name
    COLORS = (
        ('Blue','Blue'),
        ('Pink', 'Pink'),
        ('Black', 'Black'),
        ('Light-blue', 'Light-Blue'),
        ('Red', 'Red'),
        ('Green', 'Green')
    )

    SIZE = (
        ('XXL', 'XXL'),
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S'),
        ('XS','XS')
    )
    name = models.CharField(max_length=200, blank= True)
    size= models.CharField(max_length=200, choices= SIZE)
    color = models.CharField(max_length=200, choices=COLORS, blank = True)
    description = models.TextField((""), blank= True)
    is_new = models.BooleanField(default=False)
    price = models.BigIntegerField(default= False)
    #Define default String to return the name for representing the Model object."
    def __str__(self):
      return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
       return reverse('scrub-detail', args=[str(self.id)])

