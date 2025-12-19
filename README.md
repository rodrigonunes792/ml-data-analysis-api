# ML & Data Analysis API

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A powerful Machine Learning and Data Analysis API built with FastAPI, providing automated exploratory data analysis, visualizations, and ML model predictions.

**Author:** Rodrigo Nunes

## 🎯 Overview

This API provides a comprehensive suite of data analysis and machine learning capabilities, allowing users to upload datasets, perform automated analysis, generate visualizations, and make predictions using pre-trained ML models.

## ✨ Features

### Data Processing
- ✅ **Multiple Format Support** - CSV, Excel, JSON file uploads
- ✅ **Data Validation** - Automatic schema detection and validation
- ✅ **Data Cleaning** - Handle missing values, outliers, duplicates
- ✅ **Data Transformation** - Encoding, scaling, feature engineering

### Exploratory Data Analysis (EDA)
- ✅ **Statistical Summary** - Descriptive statistics for all columns
- ✅ **Distribution Analysis** - Identify data distributions
- ✅ **Correlation Analysis** - Find relationships between variables
- ✅ **Missing Data Report** - Comprehensive missing value analysis
- ✅ **Outlier Detection** - Identify and handle outliers

### Visualizations
- ✅ **Interactive Charts** - Plotly-based interactive visualizations
- ✅ **Distribution Plots** - Histograms, box plots, violin plots
- ✅ **Correlation Heatmaps** - Visual correlation matrices
- ✅ **Scatter Plots** - Relationship visualization
- ✅ **Time Series Plots** - Temporal data visualization

### Machine Learning
- ✅ **Classification Models** - Logistic Regression, Random Forest, SVM
- ✅ **Regression Models** - Linear Regression, Ridge, Lasso
- ✅ **Model Training** - Train custom models on uploaded data
- ✅ **Predictions** - Real-time predictions via API
- ✅ **Model Evaluation** - Accuracy, precision, recall, F1-score
- ✅ **Feature Importance** - Identify key predictive features

### Technical Features
- ✅ **FastAPI Framework** - High-performance async API
- ✅ **Type Hints** - Full Python type annotations
- ✅ **Pydantic Models** - Request/response validation
- ✅ **PostgreSQL Database** - Persistent data storage
- ✅ **Redis Caching** - Performance optimization
- ✅ **JWT Authentication** - Secure API access
- ✅ **OpenAPI/Swagger** - Interactive API documentation
- ✅ **Docker Support** - Containerized deployment
- ✅ **Async/Await** - Non-blocking operations
- ✅ **pytest** - Comprehensive test suite

## 🛠️ Technology Stack

- **Python 3.11+** - Modern Python features
- **FastAPI** - High-performance web framework
- **Pydantic** - Data validation
- **SQLAlchemy** - ORM for database operations
- **PostgreSQL** - Relational database
- **Redis** - Caching layer
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **scikit-learn** - Machine learning
- **TensorFlow/Keras** - Deep learning (optional)
- **Plotly** - Interactive visualizations
- **pytest** - Testing framework
- **Docker** - Containerization

## 📋 Prerequisites

- Python 3.11 or higher
- PostgreSQL 14+
- Redis 7+
- Docker & Docker Compose (optional)

## 🚀 Getting Started

### Option 1: Run with Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/ml-data-analysis-api.git
cd ml-data-analysis-api

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f api
```

The API will be available at:
- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Option 2: Run Locally

#### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Set Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/mlapi
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

#### 4. Run Database Migrations

```bash
alembic upgrade head
```

#### 5. Start the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📚 API Documentation

### Authentication

```http
POST /api/v1/auth/register    # Register new user
POST /api/v1/auth/login       # Login and get JWT token
POST /api/v1/auth/refresh     # Refresh access token
```

### Datasets

```http
POST   /api/v1/datasets/upload      # Upload dataset
GET    /api/v1/datasets              # List all datasets
GET    /api/v1/datasets/{id}         # Get dataset details
DELETE /api/v1/datasets/{id}         # Delete dataset
```

### Analysis

```http
POST /api/v1/analysis/eda/{dataset_id}           # Perform EDA
GET  /api/v1/analysis/statistics/{dataset_id}    # Get statistics
GET  /api/v1/analysis/correlations/{dataset_id}  # Get correlations
POST /api/v1/analysis/visualize/{dataset_id}     # Generate visualization
```

### Machine Learning

```http
POST /api/v1/ml/train          # Train a new model
POST /api/v1/ml/predict        # Make predictions
GET  /api/v1/ml/models         # List available models
GET  /api/v1/ml/models/{id}    # Get model details
```

### Example Usage

#### Upload a Dataset

```bash
curl -X POST "http://localhost:8000/api/v1/datasets/upload" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "file=@data.csv" \
  -F "name=Sales Data" \
  -F "description=Monthly sales data"
```

#### Perform EDA

```bash
curl -X POST "http://localhost:8000/api/v1/analysis/eda/dataset-id" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json"
```

#### Train a Model

```bash
curl -X POST "http://localhost:8000/api/v1/ml/train" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "dataset_id": "dataset-id",
    "model_type": "random_forest",
    "target_column": "price",
    "features": ["feature1", "feature2", "feature3"]
  }'
```

#### Make Predictions

```bash
curl -X POST "http://localhost:8000/api/v1/ml/predict" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": "model-id",
    "data": {
      "feature1": 10,
      "feature2": 20,
      "feature3": 30
    }
  }'
```

## 🧪 Testing

### Run All Tests

```bash
pytest
```

### Run with Coverage

```bash
pytest --cov=app --cov-report=html
```

### Run Specific Test File

```bash
pytest tests/test_analysis.py -v
```

## 📊 Project Structure

```
ml-data-analysis-api/
├── app/
│   ├── main.py                    # FastAPI application
│   ├── config.py                  # Configuration settings
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── auth.py        # Authentication endpoints
│   │       │   ├── datasets.py    # Dataset management
│   │       │   ├── analysis.py    # EDA endpoints
│   │       │   └── ml_models.py   # ML endpoints
│   │       └── router.py          # API router
│   ├── core/
│   │   ├── security.py            # JWT and security
│   │   ├── config.py              # Core configuration
│   │   └── dependencies.py        # Dependency injection
│   ├── models/
│   │   ├── database.py            # SQLAlchemy models
│   │   └── schemas.py             # Pydantic schemas
│   ├── services/
│   │   ├── data_processor.py      # Data processing logic
│   │   ├── eda_service.py         # EDA implementation
│   │   ├── ml_service.py          # ML model training
│   │   └── visualization_service.py # Chart generation
│   └── ml_models/
│       ├── classification/        # Classification models
│       ├── regression/            # Regression models
│       └── preprocessing/         # Data preprocessing
├── tests/
│   ├── test_auth.py
│   ├── test_datasets.py
│   ├── test_analysis.py
│   └── test_ml.py
├── alembic/                       # Database migrations
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

## 🔧 Configuration

### Environment Variables

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/mlapi

# Redis
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API Settings
API_V1_PREFIX=/api/v1
PROJECT_NAME=ML & Data Analysis API
VERSION=1.0.0

# File Upload
MAX_UPLOAD_SIZE=100MB
ALLOWED_EXTENSIONS=csv,xlsx,json

# ML Settings
MODEL_STORAGE_PATH=./models
CACHE_TTL=3600
```

## 🐳 Docker Deployment

### docker-compose.yml

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/mlapi
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=mlapi
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

## 📈 Performance

- **Async Operations** - Non-blocking I/O for high concurrency
- **Redis Caching** - Cache frequently accessed data
- **Database Indexing** - Optimized query performance
- **Connection Pooling** - Efficient database connections
- **Lazy Loading** - Load data only when needed

## 🔐 Security

- **JWT Authentication** - Secure token-based auth
- **Password Hashing** - bcrypt for password storage
- **CORS Configuration** - Controlled cross-origin access
- **Rate Limiting** - Prevent API abuse
- **Input Validation** - Pydantic schema validation
- **SQL Injection Prevention** - SQLAlchemy ORM

## 🚧 Roadmap

- [ ] Add deep learning models (TensorFlow/PyTorch)
- [ ] Implement AutoML capabilities
- [ ] Add time series forecasting
- [ ] Implement clustering algorithms
- [ ] Add natural language processing
- [ ] Create web dashboard
- [ ] Add model versioning
- [ ] Implement A/B testing for models
- [ ] Add data pipeline orchestration
- [ ] Implement model monitoring

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**Rodrigo Nunes**

- GitHub: [@rodrigonunes792](https://github.com/rodrigonunes792)
- LinkedIn: [Rodrigo Nunes](https://www.linkedin.com/in/rodrigonunes79/)

## 🙏 Acknowledgments

- FastAPI documentation and community
- scikit-learn contributors
- Plotly team
- Python data science community

---

⭐ Star this repository if you find it useful!
