from django.contrib import admin
from .models import *
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_type','car_image','make','price','year','fuel','power','color')
    
class CarExtraAdmin(admin.ModelAdmin):
    list_display = ('extra_1','extra_2','extra_3','extra_4')
    
admin.site.register(Car, CarAdmin)
admin.site.register(CarExtra, CarExtraAdmin)
admin.site.register(Description)
admin.site.register(Contact)
