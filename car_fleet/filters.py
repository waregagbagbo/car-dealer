from .models import Car
import django_filters

class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ['car_category', 'make', 'price', 'release_year','model_type']