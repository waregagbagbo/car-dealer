from django.contrib import admin
from django.urls import path
from .import views
from .views import CarListView,CarDetailAccessView
from django_filters.views import FilterView
from .filters import CarFilter


#app_name = 'car_fleet'

urlpatterns = [
    #('search',views.CarView, name='search'),
    path('', CarListView.as_view(), name='cars'),
    path('car/<int:pk>',CarDetailAccessView.as_view(), name='car'),  
  
]