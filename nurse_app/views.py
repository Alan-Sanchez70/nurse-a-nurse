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
from django.http import HttpResponse
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


class ScrubDeleteView(DeleteView):
    model = Scrubs
    template_name = 'nurse_app/scrubs_delete.html'  # Create a template for the delete confirmation
    success_url = reverse_lazy('scrub')  # URL to redirect to after successful deletion

