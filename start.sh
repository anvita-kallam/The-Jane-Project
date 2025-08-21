#!/bin/bash

# Jane Project Startup Script
# This script helps you get the application running quickly

echo "🚀 Jane Project - Getting Started"
echo "=================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

echo "✅ pip3 found: $(pip3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚙️  Creating .env file from template..."
    cp env.example .env
    echo "⚠️  Please edit .env file with your actual values:"
    echo "   - Set your OpenAI API key"
    echo "   - Change the SECRET_KEY"
    echo "   - Configure other settings as needed"
    echo ""
    echo "Press Enter when you're ready to continue..."
    read
fi

# Test the application
echo "🧪 Testing the application..."
python3 test_app.py

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup complete! Starting the application..."
    echo "🌐 Open http://localhost:5000 in your browser"
    echo "🛑 Press Ctrl+C to stop the server"
    echo ""
    
    # Start the Flask application
    python3 app.py
else
    echo ""
    echo "❌ Setup failed. Please check the errors above."
    echo "💡 Make sure you have:"
    echo "   - Python 3.8+ installed"
    echo "   - Internet connection for downloading packages"
    echo "   - Proper .env configuration"
    exit 1
fi
