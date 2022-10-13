from django.contrib import admin

from django.contrib import admin
from .models import Addproducts

# Register your models here.
class AddproductsAdmin(admin.ModelAdmin):
    search_fields = ("productsid",)
    
admin.site.register(Addproducts, AddproductsAdmin)