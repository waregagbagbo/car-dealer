from django.contrib import admin
from django.urls import path
from .filters import CarListingFilter
from django_filters.views import FilterView
from .views import CarListView,CarDetailAccessView


app_name = 'car_fleet'

urlpatterns = [
    path('',CarListView.as_view(), name='home'),
    #path('<slug:slug>',CarDetailAccessView.as_view(), name='car'),
    path('car/<int:pk>',CarDetailAccessView.as_view(), name='car'),
    
    path('search',FilterView.as_view(filterset_class=CarListingFilter, template_name='category/search_list.html'), name='search')
    
  
]