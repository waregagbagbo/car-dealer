from django.contrib import admin
from django.urls import path
from .import views
from .views import CarListView,CarDetailAccessView
from django_filters.views import FilterView
from .filters import CarFilter
from car_fleet.models import Car


#app_name = 'car_fleet'

urlpatterns = [
    path('',CarListView.as_view(), name='home'),
    path('car/<int:pk>',CarDetailAccessView.as_view(), name='car'),
    #path('search', views.CarView, name='search'),
    path("search", FilterView.as_view(filterset_class=CarFilter, template_name='search/search_list.html'), name="search"),   
  
]