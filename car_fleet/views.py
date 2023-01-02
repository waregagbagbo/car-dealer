from django.shortcuts import render
from django.urls import  reverse_lazy
from .models import *
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .filters import CarFilter
from .forms import AddListingForm


class CarListView(ListView):
    model = Car
    template_name = 'pages/car_listings.html'
    
     # method for pagination   
    def get_paginate_by(self, queryset):
        self.paginate_by = 7
        return self.paginate_by
           
    """def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CarListView, self).get_context_data(**kwargs)
        #context['listing'] = Car.objects.all()
        context['filter'] = CarFilter(self.request.GET, queryset= self.get_queryset())
        return context"""
    
    def get_context_data(self, **kwargs):
        context = super(CarListView,self).get_context_data(**kwargs)
        context['listing'] = Car.objects.all()
        return context

          

class CarDetailAccessView(DetailView):
    model = Car
    template_name ='pages/car_detail.html'
    success_url = 'home'
    
    
class ContactView(ListView):
    model = Contact
    
    def get_context_data(self, **kwargs):
        context = super(ContactView,self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context
    
    
class AddListingView(LoginRequiredMixin,CreateView):
    """ TODO: Add model to query
    add instances"""
    
    model = Car
    form_class= AddListingForm
    template_name = 'pages/new_listing.html'
    success_url = reverse_lazy('add_car')
    
    def form_valid(self, form):
        form = super(AddListingView,self).form_valid(form)        
        return form

     

       
  
       
    
  

    
 
    
    
  



