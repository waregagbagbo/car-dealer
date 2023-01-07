from .models import *
from django import forms

class AddListingForm(forms.ModelForm):    
    
    class Meta:
        model = Car
        fields = "__all__"
        exclude = ['custom_user','contact']