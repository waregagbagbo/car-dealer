from django.contrib import admin
from .models import *
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ['car_type','car_image','make','year','fuel','power','color']
    
admin.site.register(Car, CarAdmin)
admin.site.register(Extra)
admin.site.register(VehicleDescription)
admin.site.register(Contact)
