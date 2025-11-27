from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin interface for Book model"""
    list_display = ('id', 'name', 'edition', 'price')
    search_fields = ('name',)
    list_filter = ('edition',)
