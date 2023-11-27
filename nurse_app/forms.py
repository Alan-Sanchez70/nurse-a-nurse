from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#create class for project form
class ProjectForm(ModelForm):
   class Meta:
     model = Scrubs
     fields =('name','size','color', 'description', 'is_new','price')

class CreateUserForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']

class NurseForm(ModelForm):
   class Meta:
      model = Scrubs
      fields = '__all__'
      exclude = ['user']
