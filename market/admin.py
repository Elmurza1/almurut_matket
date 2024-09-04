from django.contrib import admin
from .models import Category, Product, ProductGallery


# Register your models here.


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    pass

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 4


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductGalleryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']






