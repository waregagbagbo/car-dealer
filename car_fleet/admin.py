from django.contrib import admin
from .models import *
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_type','car_image','make','price','year','fuel','power','color')
    
class ExtraAdmin(admin.ModelAdmin):
    list_display = ('extra_1','extra_2','extra_3','extra_4')
    
admin.site.register(Car, CarAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(VehicleDescription)
admin.site.register(Contact)
