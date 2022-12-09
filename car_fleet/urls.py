from django.contrib import admin
from django.urls import path
from .import views
from .views import CarListView,CarDetailAccessView
from django_filters.views import FilterView
from .filters import CarFilter

urlpatterns = [
    path('cars', CarListView.as_view(), name='home'),
    path('car/<int:pk>',CarDetailAccessView.as_view(), name='car'),  
  
]
