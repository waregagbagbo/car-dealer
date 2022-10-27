from django.shortcuts import render
from .models import *
from django.views.generic import ListView,CreateView


# Create your views here.
class IndexView(ListView):
    model = Car
    template_name = 'page/index.html'
    