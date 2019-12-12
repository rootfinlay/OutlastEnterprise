from django.contrib import admin
from .models import Clothing, Shoes, Accessories

#Admin
class ClothingAdmin(admin.ModelAdmin):
    list_display = (['ITEM_CONDITION' , 'Price' ,  'Brand' ,  'Type' , 'Description'])
    search_fields = (['ITEM_CONDITION' , 'Price' ,  'Brand' ,  'Type' , 'Description'])
    list_filter = (['Price' ,  'Brand' ,  'Type'])

class ShoesAdmin(admin.ModelAdmin):
    list_display = (['shoe_condition' , 'shoe_price' , 'shoe_brand' , 'shoe_type' , 'shoe_description'])
    search_fields = (['shoe_condition' , 'shoe_price' , 'shoe_brand' , 'shoe_type' , 'shoe_description'])
    list_filter = (['shoe_price' , 'shoe_brand' , 'shoe_type'])

class AccessoriesAdmin(admin.ModelAdmin):
    list_display = (['accessory_condition' , 'accessory_price' , 'accessory_brand' , 'accessory_type' , 'accessory_description'])
    search_fields = (['accessory_condition' , 'accessory_price' , 'accessory_brand' , 'accessory_type' , 'accessory_description'])
    list_filter = (['accessory_price' , 'accessory_brand' , 'accessory_type'])

#Register your modules here
admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
