from django.contrib import admin
from .models import Product

# Register your models here.

class modelAdnin(admin.ModelAdmin):
    
    list_display = ('product_name','price','total_product','content','img')
    
admin.site.register(Product,modelAdnin)