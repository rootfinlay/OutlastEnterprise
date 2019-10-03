from django.contrib import admin
from .models import Clothing, Shoes

#Admin
class ClothingAdmin(admin.ModelAdmin):
    list_display = (['ITEM_CONDITION' , 'Price' ,  'Brand' ,  'Type' , 'Description'])
    search_fields = (['ITEM_CONDITION' , 'Price' ,  'Brand' ,  'Type' , 'Description'])
    list_filter = (['Price' ,  'Brand' ,  'Type'])

class ShoesAdmin(admin.ModelAdmin):
    list_display = (['ITEM_CONDITION' , 'Price' ,  'Brand' ,  'Type' , 'Description'])
    search_fields = (['ITEM_CONDITION' , 'Price' ,  'Brand' ,  'Type' , 'Description'])
    list_filter = (['Price' ,  'Brand' ,  'Type'])

#Register your modules here
admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Shoes, ShoesAdmin)
