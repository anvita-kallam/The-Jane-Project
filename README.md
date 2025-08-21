# Jane Project - Advocacy Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

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

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- OpenAI API key (for AI features)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/jane-project.git
   cd jane-project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your actual values
   ```

5. **Initialize the database**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | `dev-secret-key-change-in-production` |
| `OPENAI_API_KEY` | OpenAI API key for AI features | Required |
| `FLASK_ENV` | Flask environment | `development` |
| `DATABASE_URL` | Database connection string | `sqlite:///jane_project.db` |

### OpenAI API Setup

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account and generate an API key
3. Add the key to your `.env` file:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key
   ```

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

## 🔧 Usage

### Adding a New Center

1. Navigate to **Centers** → **Add New Center**
2. Fill in the center information:
   - Name and contact details
   - Complete address (auto-geocoded)
   - Services offered
3. Submit the form to add to the database

### Content Analysis

1. Go to **Analysis** page
2. Choose analysis type:
   - **Classification**: Categorize content
   - **Sentiment**: Analyze emotional tone
   - **Fact Check**: Verify information accuracy
   - **AI Generation**: Generate fact-checked alternatives
3. Paste content and submit for analysis

### Interactive Map

1. Visit the **Map** page
2. Use filters to find specific centers:
   - Search by name or address
   - Filter by services
   - Filter by fact-check score
3. Click markers for detailed information

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

## 🔌 API Endpoints

### Centers API
- `GET /api/centers` - Retrieve all centers
- `POST /api/centers` - Add new center
- `GET /api/centers/<id>` - Get specific center
- `PUT /api/centers/<id>` - Update center
- `DELETE /api/centers/<id>` - Delete center

### Analysis API
- `POST /api/analyze` - Analyze content
- `GET /api/analysis` - Get analysis history
- `GET /api/analysis/<id>` - Get specific analysis

## 🧪 Testing

### Run Tests
```bash
python -m pytest tests/
```

### Test Coverage
```bash
python -m pytest --cov=app tests/
```

## 🚀 Deployment

### Production Setup

1. **Set production environment**
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-production-secret-key
   ```

2. **Use production WSGI server**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

3. **Set up reverse proxy** (nginx recommended)
4. **Configure SSL certificates**
5. **Set up monitoring and logging**

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings for all functions
- Include type hints where appropriate

## 📚 Documentation

- [API Documentation](docs/API.md)
- [User Guide](docs/USER_GUIDE.md)
- [Developer Guide](docs/DEVELOPER.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 🐛 Troubleshooting

### Common Issues

1. **OpenAI API Errors**
   - Verify your API key is correct
   - Check API usage limits
   - Ensure proper environment variable setup

2. **Geocoding Failures**
   - Verify address format
   - Check internet connectivity
   - Review geocoding service limits

3. **Database Issues**
   - Ensure database file permissions
   - Check SQLite installation
   - Verify database schema

### Getting Help

- [Issue Tracker](https://github.com/yourusername/jane-project/issues)
- [Discussions](https://github.com/yourusername/jane-project/discussions)
- [Wiki](https://github.com/yourusername/jane-project/wiki)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask Community** - Web framework
- **OpenAI** - AI language models
- **Leaflet.js** - Interactive maps
- **Bootstrap** - UI framework
- **scikit-learn** - Machine learning
- **OpenStreetMap** - Geocoding data

## 📞 Contact

- **Project Lead**: [Your Name](mailto:your.email@example.com)
- **Website**: [https://janeproject.org](https://janeproject.org)
- **GitHub**: [https://github.com/yourusername/jane-project](https://github.com/yourusername/jane-project)

---

**Made with ❤️ for reproductive health advocacy**
