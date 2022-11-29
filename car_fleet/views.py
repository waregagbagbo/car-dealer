from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .filters import CarFilter


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'pages/car_listings.html'
    success_url = 'login'
    
       
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CarListView, self).get_context_data(**kwargs)
        #context['listing'] = Car.objects.all()
        context['filter'] = CarFilter(self.request.GET, queryset= self.get_queryset())
        return context
          

class CarDetailAccessView(LoginRequiredMixin, DetailView):
    model = Car
    template_name ='pages/car_detail.html'
 
   
 
       
  
       
    
  

    
 
    
    
  



