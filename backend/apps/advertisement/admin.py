from django.contrib import admin
from .models import Category, City, Advert


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'title', 'category', 'city', 'views')
    search_fields = ('title', 'description')
    list_filter = ('category', 'city')