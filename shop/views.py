"""
views.py - VIEW in MVT Architecture

This file contains the business logic for handling HTTP requests and responses.
It processes user input, interacts with the model, and returns rendered templates.

Role in MVT:
- Handles HTTP requests (GET, POST)
- Processes form submissions securely
- Performs CRUD operations using Django ORM
- Passes data to templates for rendering
- Manages user feedback messages

Security Features:
- CSRF protection on all POST requests
- Input validation through Django forms
- No raw SQL queries (uses ORM)
- Safe data handling and sanitization
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm


def index(request):
    """
    Main view handling all CRUD operations for the bookshop.
    
    This view handles:
    - GET: Display all books and the form
    - GET with search parameters: Filter books by search criteria
    - POST with 'add': Create a new book
    - POST with 'update': Update an existing book
    - POST with 'delete': Delete a book
    
    Args:
        request: HttpRequest object containing metadata about the request
    
    Returns:
        HttpResponse: Rendered template with books and form
    """
    
    # Initialize variables
    selected_book = None
    form = BookForm()
    
    # Handle POST requests (Create, Update, Delete)
    if request.method == 'POST':
        action = request.POST.get('action')
        
        # CREATE: Add a new book
        if action == 'add':
            form = BookForm(request.POST)
            if form.is_valid():
                book = form.save()
                messages.success(
                    request,
                    f'Book "{book.name}" added successfully!'
                )
                return redirect('index')
            else:
                messages.error(
                    request,
                    'Error adding book. Please check the form for errors.'
                )
        
        # UPDATE: Modify an existing book
        elif action == 'update':
            book_id = request.POST.get('book_id')
            if book_id:
                book = get_object_or_404(Book, id=book_id)
                form = BookForm(request.POST, instance=book)
                if form.is_valid():
                    updated_book = form.save()
                    messages.success(
                        request,
                        f'Book "{updated_book.name}" updated successfully!'
                    )
                    return redirect('index')
                else:
                    selected_book = book
                    messages.error(
                        request,
                        'Error updating book. Please check the form for errors.'
                    )
        
        # DELETE: Remove a book
        elif action == 'delete':
            book_id = request.POST.get('book_id')
            if book_id:
                book = get_object_or_404(Book, id=book_id)
                book_name = book.name
                book.delete()
                messages.success(
                    request,
                    f'Book "{book_name}" deleted successfully!'
                )
                return redirect('index')
    
    # Handle GET requests or form for editing
    else:
        # Check if we're editing a book
        edit_id = request.GET.get('edit')
        if edit_id:
            selected_book = get_object_or_404(Book, id=edit_id)
            form = BookForm(instance=selected_book)
    
    # Retrieve all books from database using ORM (no raw SQL)
    books = Book.objects.all().order_by('id')
    
    # Handle search functionality
    search_query = request.GET.get('search', '').strip()
    
    # Apply search filter if provided
    if search_query:
        books = books.filter(name__icontains=search_query)
    
    # Prepare context data for template
    context = {
        'books': books,
        'form': form,
        'selected_book': selected_book,
        'search_query': search_query,
    }
    
    return render(request, 'shop/index.html', context)
