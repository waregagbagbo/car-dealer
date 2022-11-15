from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Car

class CarListing(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ['price','category','make0']