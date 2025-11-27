"""
forms.py - Form handling for the bookshop application

This file defines Django forms for secure input validation and processing.
The BookForm handles all CRUD operations with built-in security features.

Security Features:
- Automatic CSRF protection when used with {% csrf_token %}
- Input validation and sanitization
- Type checking for all fields
- Auto-escaping in templates
"""

from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    """
    ModelForm for the Book model.
    
    This form provides:
    - Automatic field generation from the Book model
    - Built-in validation for all fields
    - Clean, sanitized input data
    - Error messages for invalid data
    """
    
    class Meta:
        model = Book
        fields = ['name', 'edition', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book name',
                'maxlength': '200',
                'required': True
            }),
            'edition': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter edition number',
                'min': '1',
                'required': True
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
                'step': '0.01',
                'min': '0.01',
                'required': True
            }),
        }
        labels = {
            'name': 'Book Name',
            'edition': 'Edition',
            'price': 'Price ($)',
        }
    
    def clean_name(self):
        """Validate and clean the book name"""
        name = self.cleaned_data.get('name')
        if name:
            name = name.strip()
            if len(name) < 1:
                raise forms.ValidationError("Book name cannot be empty.")
        return name
    
    def clean_edition(self):
        """Validate the edition number"""
        edition = self.cleaned_data.get('edition')
        if edition is not None and edition < 1:
            raise forms.ValidationError("Edition must be a positive number.")
        return edition
    
    def clean_price(self):
        """Validate the price"""
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
