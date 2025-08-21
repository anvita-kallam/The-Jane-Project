from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
import os
import json
import openai
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import pickle
import nltk
from textblob import TextBlob
import geopy.distance
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jane_project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize database
db = SQLAlchemy(app)

# Download NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Database Models
class CPCCenter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    phone = db.Column(db.String(20))
    website = db.Column(db.String(200))
    services = db.Column(db.Text)
    content_analysis = db.Column(db.Text)
    fact_check_score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ContentAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    classification = db.Column(db.String(100))
    sentiment_score = db.Column(db.Float)
    fact_check_result = db.Column(db.Text)
    ai_generated_content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Forms
class CPCForm(FlaskForm):
    name = StringField('Center Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phone = StringField('Phone Number')
    website = StringField('Website')
    services = TextAreaField('Services Offered')
    submit = SubmitField('Add Center')

class ContentAnalysisForm(FlaskForm):
    content = TextAreaField('Content to Analyze', validators=[DataRequired()])
    analysis_type = SelectField('Analysis Type', choices=[
        ('classification', 'Content Classification'),
        ('sentiment', 'Sentiment Analysis'),
        ('fact_check', 'Fact Checking'),
        ('ai_generation', 'AI Content Generation')
    ])
    submit = SubmitField('Analyze Content')

# NLP Pipeline
class NLPPipeline:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        self.classifier = MultinomialNB()
        self.pipeline = Pipeline([
            ('vectorizer', self.vectorizer),
            ('classifier', self.classifier)
        ])
        
        # Sample training data for CPC content classification
        self.training_data = [
            ("Free pregnancy tests and ultrasounds", "medical_services"),
            ("Abortion alternatives and adoption information", "information"),
            ("Crisis pregnancy support and counseling", "counseling"),
            ("Medical misinformation about abortion", "misinformation"),
            ("Accurate medical information", "accurate_info"),
            ("Emotional manipulation tactics", "manipulation")
        ]
        
        self.train_model()
    
    def train_model(self):
        texts = [item[0] for item in self.training_data]
        labels = [item[1] for item in self.training_data]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            texts, labels, test_size=0.2, random_state=42
        )
        
        # Train the model
        self.pipeline.fit(X_train, y_train)
    
    def classify_content(self, text):
        try:
            prediction = self.pipeline.predict([text])[0]
            confidence = max(self.pipeline.predict_proba([text])[0])
            return prediction, confidence
        except:
            return "unknown", 0.0
    
    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity
    
    def fact_check_content(self, text):
        # This would integrate with fact-checking APIs in production
        # For now, return a basic analysis
        suspicious_keywords = ['100%', 'guaranteed', 'miracle', 'secret', 'never', 'always']
        suspicious_count = sum(1 for keyword in suspicious_keywords if keyword.lower() in text.lower())
        
        if suspicious_count > 2:
            return "High risk of misinformation", 0.3
        elif suspicious_count > 0:
            return "Moderate risk of misinformation", 0.6
        else:
            return "Low risk of misinformation", 0.8

# Initialize NLP pipeline
nlp_pipeline = NLPPipeline()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map_view():
    centers = CPCCenter.query.all()
    return render_template('map.html', centers=centers)

@app.route('/centers')
def centers():
    centers = CPCCenter.query.all()
    return render_template('centers.html', centers=centers)

@app.route('/add_center', methods=['GET', 'POST'])
def add_center():
    form = CPCForm()
    if form.validate_on_submit():
        # Geocode the address
        try:
            from geopy.geocoders import Nominatim
            geolocator = Nominatim(user_agent="jane_project")
            location = geolocator.geocode(form.address.data)
            
            if location:
                center = CPCCenter(
                    name=form.name.data,
                    address=form.address.data,
                    latitude=location.latitude,
                    longitude=location.longitude,
                    phone=form.phone.data,
                    website=form.website.data,
                    services=form.services.data
                )
                db.session.add(center)
                db.session.commit()
                flash('Center added successfully!', 'success')
                return redirect(url_for('centers'))
            else:
                flash('Could not geocode address. Please check the address.', 'error')
        except Exception as e:
            flash(f'Error adding center: {str(e)}', 'error')
    
    return render_template('add_center.html', form=form)

@app.route('/analysis', methods=['GET', 'POST'])
def content_analysis():
    form = ContentAnalysisForm()
    results = None
    
    if form.validate_on_submit():
        content = form.content.data
        analysis_type = form.analysis_type.data
        
        # Perform analysis based on type
        if analysis_type == 'classification':
            classification, confidence = nlp_pipeline.classify_content(content)
            results = {
                'type': 'Classification',
                'classification': classification,
                'confidence': f"{confidence:.2%}",
                'content': content
            }
        elif analysis_type == 'sentiment':
            sentiment_score = nlp_pipeline.analyze_sentiment(content)
            sentiment_label = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
            results = {
                'type': 'Sentiment Analysis',
                'sentiment': sentiment_label,
                'score': f"{sentiment_score:.3f}",
                'content': content
            }
        elif analysis_type == 'fact_check':
            fact_check_result, score = nlp_pipeline.fact_check_content(content)
            results = {
                'type': 'Fact Check',
                'result': fact_check_result,
                'score': f"{score:.1%}",
                'content': content
            }
        elif analysis_type == 'ai_generation':
            try:
                # Generate AI content using OpenAI
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that provides accurate, evidence-based information about reproductive health and pregnancy options. Always cite reliable sources and avoid misinformation."},
                        {"role": "user", "content": f"Based on this content: '{content}', generate a fact-checked, informative response that addresses any inaccuracies or provides additional context."}
                    ],
                    max_tokens=300
                )
                
                ai_content = response.choices[0].message.content
                results = {
                    'type': 'AI Content Generation',
                    'ai_content': ai_content,
                    'content': content
                }
            except Exception as e:
                results = {
                    'type': 'AI Content Generation',
                    'error': f"OpenAI API error: {str(e)}",
                    'content': content
                }
        
        # Save analysis to database
        if results:
            analysis = ContentAnalysis(
                content=content,
                classification=results.get('classification', ''),
                sentiment_score=results.get('score', 0.0) if 'score' in results else None,
                fact_check_result=results.get('result', ''),
                ai_generated_content=results.get('ai_content', '')
            )
            db.session.add(analysis)
            db.session.commit()
    
    return render_template('analysis.html', form=form, results=results)

@app.route('/api/centers')
def api_centers():
    centers = CPCCenter.query.all()
    centers_data = []
    
    for center in centers:
        centers_data.append({
            'id': center.id,
            'name': center.name,
            'address': center.address,
            'latitude': center.latitude,
            'longitude': center.longitude,
            'phone': center.phone,
            'website': center.website,
            'services': center.services,
            'fact_check_score': center.fact_check_score
        })
    
    return jsonify(centers_data)

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json()
    content = data.get('content', '')
    
    if not content:
        return jsonify({'error': 'Content is required'}), 400
    
    # Perform comprehensive analysis
    classification, confidence = nlp_pipeline.classify_content(content)
    sentiment_score = nlp_pipeline.analyze_sentiment(content)
    fact_check_result, fact_score = nlp_pipeline.fact_check_content(content)
    
    return jsonify({
        'classification': classification,
        'confidence': confidence,
        'sentiment_score': sentiment_score,
        'fact_check_result': fact_check_result,
        'fact_score': fact_score
    })

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
