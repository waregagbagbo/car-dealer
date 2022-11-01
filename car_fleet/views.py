from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView
from django.core.paginator import Paginator


# Create your views here.
class CarListView(ListView):
    model = Car
    template_name = 'page/index.html'
    paginate_by = 4 
     
       
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CarListView, self).get_context_data(**kwargs)
        context['listing'] = Car.objects.all()
        return context

