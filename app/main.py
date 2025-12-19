from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import api_router

# CORS Configuration Constants
CORS_ALLOWED_ORIGINS = ["*"]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_METHODS = ["*"]
CORS_ALLOWED_HEADERS = ["*"]

app = FastAPI(
        title="ML & Data Analysis API",
        description="API for Exploratory Data Analysis and Automated Machine Learning",
        version="1.0.0"
)

# CORS Middleware Configuration
app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ALLOWED_ORIGINS,
        allow_credentials=CORS_ALLOW_CREDENTIALS,
        allow_methods=CORS_ALLOWED_METHODS,
        allow_headers=CORS_ALLOWED_HEADERS,
)

# Routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
        return {"message": "Welcome to ML & Data Analysis API. Visit /docs for documentation."}
