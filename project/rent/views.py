from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from rent.models import Rental
from rent.forms import RentalForm

# Create your views here.
class RentListView(ListView):
    template_name = 'index.html'
    model = Rental
    queryset = Rental.objects.all()
    context_object_name = 'rent_list'

class RentDetailView(DetailView):
    model = Rental
    template_name = 'rent_detail.html'
    context_object_name = 'rent'

class RentCreateView(CreateView):
    form_class = Rental
    template_name = 'rent_create.html'

