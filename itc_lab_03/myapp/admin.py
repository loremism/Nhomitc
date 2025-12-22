from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}  # Tự động điền slug từ name


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'featured', 'created_at']
    list_filter = ['category', 'featured', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'featured']  # Có thể sửa giá và featured ngay trong danh sách
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at']