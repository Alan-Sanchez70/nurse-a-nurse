from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('scrubs/', views.ScrubsListView.as_view(), name= 'scrub'),
path('scrubs/<int:pk>', views.ScrubsDetailView.as_view(), name='scrub-detail'),
path('scrubs/create_project/', views.createProject, name='create_scrub'),
path('scrubs/<int:pk>/delete/', views.ScrubDeleteView.as_view(), name='scrub-delete'),

]
