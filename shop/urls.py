"""
urls.py - URL routing for the shop app

This file maps URLs to views, defining the application's routing structure.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main page with CRUD operations
]
