#!/usr/bin/env python3
"""
Simple test script for Jane Project Flask application
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported"""
    try:
        import flask
        print("✓ Flask imported successfully")
        
        import openai
        print("✓ OpenAI imported successfully")
        
        import sklearn
        print("✓ scikit-learn imported successfully")
        
        import pandas
        print("✓ Pandas imported successfully")
        
        import numpy
        print("✓ NumPy imported successfully")
        
        import nltk
        print("✓ NLTK imported successfully")
        
        import geopy
        print("✓ Geopy imported successfully")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_flask_app():
    """Test that the Flask app can be created"""
    try:
        from app import app
        print("✓ Flask app created successfully")
        
        # Test basic app configuration
        assert app.config['SECRET_KEY'] is not None
        print("✓ App configuration valid")
        
        return True
    except Exception as e:
        print(f"✗ Flask app error: {e}")
        return False

def test_database():
    """Test database connection and models"""
    try:
        from app import db, CPCCenter, ContentAnalysis
        
        print("✓ Database models imported successfully")
        
        # Test model attributes
        assert hasattr(CPCCenter, 'name')
        assert hasattr(CPCCenter, 'address')
        assert hasattr(CPCCenter, 'latitude')
        assert hasattr(CPCCenter, 'longitude')
        
        assert hasattr(ContentAnalysis, 'content')
        assert hasattr(ContentAnalysis, 'classification')
        
        print("✓ Database models valid")
        
        return True
    except Exception as e:
        print(f"✗ Database error: {e}")
        return False

def test_nlp_pipeline():
    """Test NLP pipeline functionality"""
    try:
        from app import nlp_pipeline
        
        # Test basic functionality
        test_text = "Free pregnancy tests and ultrasounds available"
        classification, confidence = nlp_pipeline.classify_content(test_text)
        
        assert classification is not None
        assert confidence >= 0 and confidence <= 1
        
        print("✓ NLP pipeline working")
        
        return True
    except Exception as e:
        print(f"✗ NLP pipeline error: {e}")
        return False

def test_routes():
    """Test that all routes are properly defined"""
    try:
        from app import app
        
        # Check for essential routes
        routes = [str(rule) for rule in app.url_map.iter_rules()]
        
        essential_routes = [
            '/',
            '/map',
            '/centers',
            '/analysis',
            '/about',
            '/contact'
        ]
        
        for route in essential_routes:
            if route in routes:
                print(f"✓ Route {route} found")
            else:
                print(f"✗ Route {route} missing")
                return False
        
        print("✓ All essential routes present")
        return True
    except Exception as e:
        print(f"✗ Routes error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Jane Project Application...\n")
    
    tests = [
        ("Import Tests", test_imports),
        ("Flask App Tests", test_flask_app),
        ("Database Tests", test_database),
        ("NLP Pipeline Tests", test_nlp_pipeline),
        ("Route Tests", test_routes)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        try:
            if test_func():
                passed += 1
                print(f"✓ {test_name} passed\n")
            else:
                print(f"✗ {test_name} failed\n")
        except Exception as e:
            print(f"✗ {test_name} error: {e}\n")
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to run.")
        print("\nTo start the application:")
        print("1. Set up your .env file with required variables")
        print("2. Run: python app.py")
        print("3. Open http://localhost:5000 in your browser")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
