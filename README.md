# The Jane Project - Advocacy Platform

An open-source advocacy platform empowering communities with accurate information, geospatial data visualization, and AI-powered fact-checking for reproductive health awareness.

## 🌟 Features

### 🗺️ Geospatial Data Visualization
- **Interactive Maps**: Powered by Leaflet.js with real-time data
- **Crisis Pregnancy Center Database**: Comprehensive location and service information
- **Advanced Filtering**: Search by location, services, and fact-check scores
- **Geocoding**: Automatic address-to-coordinate conversion

### 🤖 AI-Powered Analysis
- **Content Classification**: ML-based categorization using scikit-learn
- **Sentiment Analysis**: Emotional tone and bias detection
- **Fact-Checking**: Automated misinformation detection algorithms
- **AI Content Generation**: OpenAI-powered fact-checked alternatives

### 📊 Data Management
- **SQLite Database**: Lightweight, portable data storage
- **RESTful API**: Clean endpoints for data access and manipulation
- **Data Validation**: Comprehensive input validation and sanitization
- **Export Capabilities**: Data export in multiple formats

### 🎨 Modern User Interface
- **Responsive Design**: Mobile-first Bootstrap 5 implementation
- **Interactive Charts**: Chart.js integration for data visualization
- **Accessibility**: WCAG compliant design patterns
- **Progressive Enhancement**: Works without JavaScript


## 📁 Project Structure

```
janeProj/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── env.example           # Environment variables template
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Homepage
│   ├── map.html         # Interactive map
│   ├── centers.html     # Centers directory
│   ├── analysis.html    # Content analysis
│   ├── add_center.html  # Add center form
│   ├── about.html       # About page
│   ├── contact.html     # Contact page
│   ├── 404.html         # 404 error page
│   └── 500.html         # 500 error page
└── static/              # Static assets
    ├── css/
    │   └── style.css    # Main stylesheet
    ├── js/
    │   └── main.js      # Main JavaScript
    └── images/          # Image assets
```


## 🧠 AI Features

### Content Classification
The platform uses a trained scikit-learn model to classify content into categories:
- Medical services
- Information provision
- Counseling services
- Misinformation detection
- Accurate information
- Manipulation tactics

### Fact-Checking Algorithm
Our fact-checking system analyzes content for:
- Suspicious keywords and phrases
- Emotional manipulation indicators
- Inconsistent claims
- Source credibility assessment

### OpenAI Integration
- **Content Generation**: Fact-checked alternatives to problematic content
- **Information Enhancement**: AI-powered content improvement
- **Bias Detection**: Advanced language model analysis

## 🗄️ Database Schema

### CPCCenter Model
```python
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
```

### ContentAnalysis Model
```python
class ContentAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    classification = db.Column(db.String(100))
    sentiment_score = db.Column(db.Float)
    fact_check_result = db.Column(db.Text)
    ai_generated_content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```


vocacy**
