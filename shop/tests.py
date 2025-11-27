from django.test import TestCase
from .models import Book
from decimal import Decimal


class BookModelTest(TestCase):
    """Test cases for the Book model"""
    
    def test_create_book(self):
        """Test creating a book"""
        book = Book.objects.create(
            name="Django for Beginners",
            edition=1,
            price=Decimal('29.99')
        )
        self.assertEqual(book.name, "Django for Beginners")
        self.assertEqual(book.edition, 1)
        self.assertEqual(book.price, Decimal('29.99'))
    
    def test_book_string_representation(self):
        """Test the __str__ method"""
        book = Book(name="Python Crash Course", edition=2)
        self.assertEqual(str(book), "Python Crash Course (Edition 2)")
