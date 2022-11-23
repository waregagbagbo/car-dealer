from .models import *
import django_filters

class CarFilter(django_filters.FilterSet):
    year_manufactured = django_filters.NumberFilter(field_name='release_year')
    
    class Meta:
       model = Car
       fields = ['make','model_type','price','color','fuel']

    
  
    
    