"""
models.py - MODEL in MVT Architecture

This file defines the data structure for the bookshop application.
The Book model represents a book entity with fields: name, edition, and price.

Role in MVT:
- Defines database schema using Django ORM
- Handles data validation at the model level
- Provides an abstraction layer over raw SQL
- Maps Python classes to database tables
"""

from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Book(models.Model):
    """
    Book model representing a book in the bookshop.
    
    Fields:
        name: The title of the book (max 200 characters)
        edition: The edition number of the book (positive integer)
        price: The price of the book (decimal with 2 decimal places, must be positive)
    """
    name = models.CharField(
        max_length=200,
        verbose_name="Book Name",
        help_text="Enter the title of the book"
    )
    
    edition = models.PositiveIntegerField(
        verbose_name="Edition",
        help_text="Enter the edition number"
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Price",
        help_text="Enter the price (must be positive)"
    )
    
    class Meta:
        ordering = ['id']  # Default ordering by ID
        verbose_name = "Book"
        verbose_name_plural = "Books"
    
    def __str__(self):
        """String representation of the Book object"""
        return f"{self.name} (Edition {self.edition})"
