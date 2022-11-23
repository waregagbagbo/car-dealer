from .models import *
import django_filters

class CarFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(field_name='car_category',choices=CAR_CATEGORY)
    
   # year_manufactured = django_filters.NumberFilter(field_name='release_year')
    
    class Meta:
       model = Car
       fields = ['category','make','model_type','price','color','fuel']

    
  
    
    