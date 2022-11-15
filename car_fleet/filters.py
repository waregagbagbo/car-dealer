from .models import Car
import django_filters

class CarListingFilter(django_filters.FilterSet):
    make = django_filters.CharFilter(lookup_expr='icontains')
    released_year = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
        
        
        
