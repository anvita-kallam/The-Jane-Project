# Jane Project - Setup Guide

## 🚀 Quick Start (Recommended)

The easiest way to get started is to use our automated startup script:

```bash
./start.sh
```

This script will:
- Check your Python installation
- Create a virtual environment
- Install all dependencies
- Set up your environment file
- Test the application
- Start the server

## 📋 Manual Setup

If you prefer to set up manually or the automated script doesn't work:

### 1. Prerequisites

- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **pip** - Usually comes with Python
- **OpenAI API Key** - [Get one here](https://platform.openai.com/)

### 2. Clone and Navigate

```bash
git clone <your-repo-url>
cd jane-project
```

### 3. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Environment Configuration

```bash
cp env.example .env
```

Edit `.env` file with your values:
```bash
# Required
OPENAI_API_KEY=sk-your-actual-api-key-here
SECRET_KEY=your-super-secret-key-change-this

# Optional (for production)
FLASK_ENV=production
DEBUG=False
```

### 6. Test Installation

```bash
python3 test_app.py
```

### 7. Start Application

```bash
python3 app.py
```

Open http://localhost:5000 in your browser!

## 🔧 Troubleshooting

### Common Issues

#### Python Not Found
```bash
# Check Python version
python3 --version

# If not found, install Python 3.8+
# macOS: brew install python3
# Ubuntu: sudo apt install python3 python3-pip
# Windows: Download from python.org
```

#### pip Not Found
```bash
# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

#### Permission Errors
```bash
# Make startup script executable
chmod +x start.sh

# Use sudo if needed (not recommended)
sudo python3 -m pip install -r requirements.txt
```

#### OpenAI API Errors
- Verify your API key is correct
- Check your OpenAI account has credits
- Ensure the key has proper permissions

#### Geocoding Failures
- Check internet connection
- Verify address format
- OpenStreetMap service might be temporarily down

### Dependency Issues

If you encounter specific package installation problems:

```bash
# Try upgrading pip first
pip install --upgrade pip

# Install packages individually
pip install flask
pip install openai
pip install scikit-learn
pip install pandas
pip install numpy
pip install nltk
pip install geopy

# Or use conda if you prefer
conda install flask openai scikit-learn pandas numpy nltk geopy
```

### Database Issues

```bash
# Remove existing database
rm jane_project.db

# Restart application (it will recreate the database)
python3 app.py
```

## 🌐 Production Deployment

### Using Gunicorn

```bash
# Install gunicorn
pip install gunicorn

# Start with multiple workers
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Using Docker

```bash
# Build image
docker build -t jane-project .

# Run container
docker run -p 8000:8000 jane-project
```

### Environment Variables for Production

```bash
export FLASK_ENV=production
export SECRET_KEY=your-production-secret-key
export OPENAI_API_KEY=your-production-api-key
export DATABASE_URL=postgresql://user:pass@localhost/dbname
```

## 📱 Mobile Development

The application is mobile-responsive by default. For mobile-specific development:

```bash
# Test mobile view in browser
# Open DevTools → Toggle device toolbar
# Or use browser extensions like "Mobile/Responsive Web Design Tester"
```

## 🔍 Testing

### Run All Tests
```bash
python3 test_app.py
```

### Individual Test Categories
```bash
# Test imports only
python3 -c "from test_app import test_imports; test_imports()"

# Test Flask app
python3 -c "from test_app import test_flask_app; test_flask_app()"

# Test database
python3 -c "from test_app import test_database; test_database()"
```

## 📊 Monitoring

### Check Application Status
```bash
# Check if Flask is running
curl http://localhost:5000

# Check database
ls -la jane_project.db

# Check logs (if configured)
tail -f logs/jane_project.log
```

### Performance Monitoring
```bash
# Monitor CPU/Memory usage
top -p $(pgrep -f "python3 app.py")

# Check disk space
df -h
```

## 🆘 Getting Help

### Before Asking for Help

1. **Check this guide** - Your issue might be covered here
2. **Run the test script** - `python3 test_app.py`
3. **Check error logs** - Look for specific error messages
4. **Verify environment** - Ensure `.env` is properly configured

### When Asking for Help

Include:
- Your operating system and Python version
- Complete error message
- Steps you've already tried
- Contents of your `.env` file (remove sensitive data)

### Support Channels

- **GitHub Issues** - For bug reports and feature requests
- **GitHub Discussions** - For questions and community help
- **Documentation** - Check the main README.md
- **Code Examples** - Look at the test files

## 🎯 Next Steps

Once you have the application running:

1. **Explore the interface** - Navigate through all pages
2. **Add sample data** - Use the "Add Center" form
3. **Test AI features** - Try content analysis
4. **Customize** - Modify templates and styles
5. **Deploy** - Move to production environment
6. **Contribute** - Submit improvements and bug fixes

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Leaflet.js Documentation](https://leafletjs.com/reference.html)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

---

**Happy coding! 🚀**
