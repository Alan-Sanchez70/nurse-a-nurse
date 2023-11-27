from typing import Any
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic 
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.shortcuts import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin

#paypal imports
import paypalrestsdk
from django.conf import settings
from django.urls import reverse

# Create your views here.
def index(request):
    nurse_active = Scrubs.objects.filter(is_new=True)
    #print("active portfolio query set", nurse_active)
    return render( request, 'nurse_app/index.html', {'nurse_active':nurse_active})


#scrub classes
#these classes contain the templates of how are going to be display and getting the queries fro the database.
class ScrubsListView(generic.ListView):
   model = Scrubs
   
   def scrub_list_view(request):
        scrubs_list = Scrubs.objects.all()  # Fetch all Scrub objects from the database
        return render(request, 'nurse_app/scrubs_list.html', {'scrub_list': scrubs_list})
class ScrubsDetailView(generic.DetailView):
   model = Scrubs

   def scrub_detail(self, request, pk):
        scrubs = Scrubs.objects.get(pk=pk)  # Retrieve the specific Scrub object
        return render(request, 'scrubs_detail.html', {'scrub': scrubs})

@login_required(login_url= 'login')
@allowed_users(allowed_roles=['Nurse members'])
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Create a new Scrub object
            new_scrub = form.save()
            # Redirect to the detail view of the new Scrub object
            return redirect('scrub-detail', pk=new_scrub.pk)
    
    # Handle GET request or form errors
    return render(request, 'nurse_app/scrubs_form.html', {'form': form})


class ScrubDeleteView(LoginRequiredMixin, DeleteView):
    model = Scrubs
    template_name = 'nurse_app/scrubs_delete.html'  # Create a template for the delete confirmation
    success_url = reverse_lazy('scrub')  # URL to redirect to after successful deletion


class ScrubUpdateView(LoginRequiredMixin, UpdateView):
    model = Scrubs
    template_name = 'nurse_app/scrubs_update.html'  # Create a template for the edit form
    fields = ['name', 'color', 'size', 'description', 'is_new', 'price']  # Fields to edit
    success_url = reverse_lazy('scrub')  # URL to redirect to after successful edit

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name = 'Nurse members')
            user.groups.add(group)
            #nurse = Scrubs.objects.create(user=user)
            #nurse.save()

            messages.success(request, 'Account is created for ' + username)
            return redirect('login')
    
    context = {'form' : form}
    return render(request, 'registration/register.html', context)

@login_required(login_url= 'login')
@allowed_users(allowed_roles=['Nurse members'])
def userPage(request):
    nurse = request.user.scrub
    form = NurseForm(instance = nurse)
    print('nurse', nurse)
    return render(request, 'nurse_app/user.html')

#paypal implementation
#paypalrestsdk.configure({
 #   "mode" : "Sandbox", 
  #  "Client_id" : settings.PAYPAL_CLIENT_ID,
   # "client_secret": settings.PAYPAL_SECRET,

#})

#creating payment
def create_payment(request):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer":{
            "payment_method": "paypal",
        },
        "redirect_urls":{
            "return_url": request.build_absolute_uri(reverse('execute_payment')),
            "cancel_url":request.build_absolute_uri(reverse('payment_failed')),     
        },
        "transactions":[
            {
                "amount":{
                    "total": "10.00",
                    "currrency": "USD",
                },
                "description": "Payment for Product/Service"
            }
        ],
    })

    if payment.create():
        return redirect(payment.link[1].href)
    else:
        return render(request, 'payment_failed.html')


def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment =paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'payment_success.html')
    else:
         return render(request, 'payment_failed.html')

def payment_checkout(request):
    return render(request, 'checkout.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')

