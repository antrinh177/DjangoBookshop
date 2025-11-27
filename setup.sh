#!/bin/bash

# Secure Django Bookshop - Quick Setup Script
# This script helps set up the application quickly

echo "Secure Django Bookshop Application - Setup Script"
echo "=================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
echo "🔧 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Make sure MySQL is running"
echo "2. Create the database: CREATE DATABASE bookshop_db;"
echo "3. Update database credentials in bookshop_project/settings.py"
echo "4. Run migrations:"
echo "   python manage.py makemigrations"
echo "   python manage.py migrate"
echo "5. Start the server:"
echo "   python manage.py runserver"
echo ""
echo "See README.md for detailed instructions"
