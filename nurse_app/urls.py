from django.urls import path
from django.urls import include
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
path('scrubs/<int:pk>/edit/', views.ScrubUpdateView.as_view(), name='scrub-edit'),
path('accounts/', include('django.contrib.auth.urls')),
path('accounts/register/', views.registerPage, name = 'register_page'),
path('user/', views.userPage, name = 'user_page'),

path('checkout/', views.payment_checkout, name='checkout_payment'),
path('create_payment/', views.create_payment, name='create_payment'),
path('execute_payment/', views.execute_payment, name='execute_payment'),
path('payment_failed/', views.payment_failed, name='payment_failed'),

]
