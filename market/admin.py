from django.contrib import admin
from .models import Category, Product, ProductGallery, ProductUserRating, WeatherData


# Register your models here.

@admin.register(ProductUserRating)
class ProductUserRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating']

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


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['city', 'temperature']






