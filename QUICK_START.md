## Setup Guide

### 1. Install Dependencies
```bash
cd /Users/antrinh/Documents/Files/Courses/Semester3/CPAN214HighLevel/projects/personal/bookshop_project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install django mysqlclient
```

### 2. Setup MySQL Database
```bash
# Start MySQL
brew services start mysql  # macOS
# or
mysql.server start

# Create database
mysql -u root -p
```

In MySQL prompt:
```sql
CREATE DATABASE bookshop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### 3. Configure Database
Edit `bookshop_project/settings.py` line 77-86:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookshop_db',
        'USER': 'root',          # ← Your MySQL username
        'PASSWORD': 'yourpass',  # ← Your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server
```bash
python manage.py runserver
```

### 6. Open in Browser
```
http://127.0.0.1:8000/
```

---

## Troubleshooting

### Error: "No module named 'MySQLdb'"
```bash
# Solution 1: Install mysqlclient
pip install mysqlclient

# Solution 2: Use pymysql instead
pip install pymysql
```

Then add to `bookshop_project/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### Error: "Access denied for user"
- Check MySQL username and password in `settings.py`
- Make sure MySQL server is running
- Try: `mysql -u root -p` to test connection

### Error: "Unknown database 'bookshop_db'"
```sql
-- Create the database
CREATE DATABASE bookshop_db;
```

### Port Already in Use
```bash
# Use a different port
python manage.py runserver 8001
```

---