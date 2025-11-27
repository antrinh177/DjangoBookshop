# 📚 Secure Django Bookshop Application

A secure, full-featured CRUD web application built with Django that manages bookshop records using the MVT (Model-View-Template) architecture and MySQL database.

## 🎯 Project Overview

This application demonstrates:
- **Complete CRUD Operations**: Create, Read, Update, and Delete books
- **MVT Architecture**: Clean separation of data, logic, and presentation
- **Security Best Practices**: CSRF protection, input validation, and safe rendering
- **Django ORM**: No raw SQL queries
- **User Feedback**: Success and error messages for all actions

## 📋 Features

✅ Add new books with name, edition, and price  
✅ View all books in a formatted table  
✅ Update existing book records  
✅ Delete books with confirmation  
✅ Highlight selected rows during editing  
✅ Form validation and error handling  
✅ Responsive design with modern UI  
✅ CSRF protection on all forms  
✅ Auto-escaping of user input  

## 🏗️ Project Structure

```
bookshop_project/
├── bookshop_project/
│   ├── __init__.py
│   ├── settings.py          # Configuration & MySQL setup
│   ├── urls.py              # Project-level URL routing
│   ├── asgi.py              # ASGI configuration
│   └── wsgi.py              # WSGI configuration
├── shop/
│   ├── __init__.py
│   ├── models.py            # M: Book model (Database schema)
│   ├── views.py             # V: Business logic & request handling
│   ├── forms.py             # BookForm for validation
│   ├── urls.py              # App-level URL routing
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── tests.py             # Unit tests
│   └── templates/
│       └── shop/
│           └── index.html   # T: User interface template
├── manage.py                # Django CLI tool
└── README.md                # This file
```

## 🔍 MVT Architecture Explanation

### 📊 Model (`models.py`)

**Role in MVT**: Defines the data structure and database schema.

The `Book` model represents the data layer:
- **Purpose**: Defines what data is stored and how it's structured
- **Responsibilities**:
  - Defines database fields (name, edition, price)
  - Implements data validation at the model level
  - Provides an abstraction over raw SQL
  - Maps Python classes to database tables automatically

**Key Features**:
```python
class Book(models.Model):
    name = models.CharField(max_length=200)          # Book title
    edition = models.PositiveIntegerField()          # Edition number
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price
```

**Security**: 
- Field-level validation (max length, positive integers, decimal precision)
- ORM prevents SQL injection attacks
- Type safety through Django's field types

### 🎮 View (`views.py`)

**Role in MVT**: Contains the business logic and handles HTTP requests/responses.

The `index` view is the controller that:
- **Purpose**: Processes user input and coordinates Model and Template
- **Responsibilities**:
  - Handles GET requests (display data)
  - Handles POST requests (create, update, delete)
  - Validates form submissions
  - Queries the database using Django ORM
  - Passes data to templates
  - Manages user feedback messages

**CRUD Operations**:
1. **Create**: `form.save()` - Validates and saves new book
2. **Read**: `Book.objects.all()` - Retrieves all books
3. **Update**: `form.save()` with instance - Updates existing book
4. **Delete**: `book.delete()` - Removes book from database

**Security**:
- CSRF token validation on all POST requests
- Input validation through Django forms
- Uses `get_object_or_404()` to prevent invalid queries
- No raw SQL queries
- Sanitized error messages

### 🎨 Template (`index.html`)

**Role in MVT**: Defines how data is presented to the user.

The template is the presentation layer:
- **Purpose**: Renders dynamic HTML for the user interface
- **Responsibilities**:
  - Displays book data in a table
  - Renders forms for user input
  - Shows feedback messages
  - Highlights selected rows
  - Provides interactive CRUD interface

**Django Template Language (DTL) Features**:
```django
{% csrf_token %}              # CSRF protection
{{ book.name }}               # Auto-escaped output
{% for book in books %}       # Iteration
{% if selected_book %}        # Conditional rendering
{{ books.count }}             # Template filters
```

**Security**:
- Automatic HTML escaping prevents XSS attacks
- CSRF tokens in all forms
- No sensitive data exposure
- Safe rendering of user input

## 🔒 Security Features

### 1. CSRF Protection
```django
{% csrf_token %}
```
Every form includes a CSRF token to prevent Cross-Site Request Forgery attacks.

### 2. Input Validation
```python
# In forms.py
def clean_name(self):
    name = self.cleaned_data.get('name')
    if len(name.strip()) < 1:
        raise forms.ValidationError("Book name cannot be empty.")
    return name
```
All user input is validated before processing.

### 3. Safe Rendering
```django
{{ book.name }}  <!-- Automatically escaped -->
```
Django automatically escapes HTML to prevent XSS attacks.

### 4. ORM (No Raw SQL)
```python
# ✅ Secure: Using ORM
books = Book.objects.all()

# ❌ Insecure: Raw SQL (NOT USED)
# cursor.execute("SELECT * FROM books")
```
Django ORM prevents SQL injection attacks.

### 5. Secure Form Handling
```python
if form.is_valid():
    form.save()  # Only saves if validation passes
```
Forms validate data types, ranges, and constraints.

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- MySQL Server 5.7 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project
```bash
cd /Users/antrinh/Documents/Files/Courses/Semester3/CPAN214HighLevel/projects/personal/bookshop_project
```

### Step 2: Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### Step 3: Install Dependencies
```bash
pip install django mysqlclient
```

**Alternative** (if mysqlclient fails):
```bash
pip install django pymysql
```

Then add to `bookshop_project/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### Step 4: Configure MySQL Database

1. **Start MySQL Server**
   ```bash
   # macOS (with Homebrew)
   brew services start mysql
   
   # Or start manually
   mysql.server start
   ```

2. **Create the Database**
   ```bash
   mysql -u root -p
   ```
   
   In MySQL prompt:
   ```sql
   CREATE DATABASE bookshop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   EXIT;
   ```

3. **Update Database Credentials**
   
   Edit `bookshop_project/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'bookshop_db',
           'USER': 'root',        # Your MySQL username
           'PASSWORD': '',        # Your MySQL password
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 7: Run the Development Server
```bash
python manage.py runserver
```

### Step 8: Access the Application
Open your browser and navigate to:
- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🎮 Usage Guide

### Adding a Book
1. Fill in the form fields (Name, Edition, Price)
2. Click "Add Book"
3. Success message appears and book is added to the table

### Updating a Book
1. Click "Edit" button on the desired book row
2. The row highlights in yellow
3. Form populates with book data
4. Modify the fields
5. Click "Update Book"

### Deleting a Book
1. Click "Delete" button on the desired book row
2. Confirm the deletion in the popup
3. Book is removed and success message appears

### Viewing Books
- All books are displayed in the table
- Table shows: ID, Name, Edition, Price
- Empty state message appears when no books exist

## 🧪 Testing

Run the included unit tests:
```bash
python manage.py test shop
```

## 📚 Learning Outcomes

By studying this project, you will understand:

1. **Django MVT Architecture**
   - How Model, View, and Template work together
   - Separation of concerns in web applications

2. **Database Integration**
   - Using Django ORM instead of raw SQL
   - Creating models and running migrations
   - CRUD operations with the database

3. **Form Handling**
   - ModelForms for automatic form generation
   - Server-side validation
   - Error handling and user feedback

4. **Security Best Practices**
   - CSRF protection implementation
   - Input validation and sanitization
   - XSS and SQL injection prevention

5. **Template Rendering**
   - Django Template Language (DTL)
   - Dynamic content rendering
   - Template inheritance and filters

## 🛠️ Technologies Used

- **Backend**: Django 4.2+
- **Database**: MySQL 5.7+
- **Frontend**: HTML5, CSS3 (embedded)
- **Architecture**: MVT (Model-View-Template)
- **Security**: Django's built-in security features

## 📝 Assignment Deliverables

This project fulfills all requirements:

✅ **Functionality**
- Complete CRUD operations
- Form-based input
- Table display with all required columns
- Row highlighting for editing
- Feedback messages

✅ **Security**
- CSRF protection in all forms
- Input validation via Django forms
- Safe rendering (auto-escaping)
- No raw SQL (Django ORM only)
- No sensitive data exposure

✅ **Implementation**
- Proper MVT architecture
- Django forms and ORM
- Clean code structure
- Following Django best practices

✅ **Documentation**
- Complete README
- Code comments
- MVT explanations
- Setup instructions

## 🎓 MVT vs MVC

**MVT (Django)** vs **MVC (Traditional)**:

| MVT (Django) | MVC (Traditional) | Description |
|--------------|-------------------|-------------|
| Model | Model | Data structure & database |
| View | Controller | Business logic |
| Template | View | User interface |

Django's "View" is equivalent to a "Controller" in MVC, and Django's "Template" is equivalent to a "View" in MVC.

## 🐛 Troubleshooting

### MySQL Connection Error
```bash
# Make sure MySQL is running
brew services list  # macOS
sudo service mysql status  # Linux

# Check credentials in settings.py
```

### mysqlclient Installation Error
```bash
# Install MySQL dependencies
brew install mysql  # macOS
sudo apt-get install python3-dev libmysqlclient-dev  # Linux

# Or use pymysql as alternative
pip install pymysql
```

### Migration Errors
```bash
# Reset migrations (CAUTION: deletes data)
python manage.py migrate shop zero
python manage.py makemigrations
python manage.py migrate
```

## 👤 Author

**Student Name**: An Trinh  
**Course**: CPAN214 - High Level Programming  
**Semester**: 3  
**Date**: November 26, 2025

---