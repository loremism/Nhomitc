from django.contrib import admin
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'Size', 'color')
    list_filter = ('category',)
    search_fields = ('name', 'description')

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category)

# Register your models here.