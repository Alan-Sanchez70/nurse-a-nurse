from django.forms import ModelForm
from .models import *

#create class for project form
class ProjectForm(ModelForm):
   class Meta:
     model = Scrubs
     fields =('name','size','color', 'description', 'is_new','price')
