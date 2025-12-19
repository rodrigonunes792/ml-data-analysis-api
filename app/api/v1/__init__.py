from fastapi import APIRouter
from app.api.v1.endpoints import analysis, ml

api_router = APIRouter()

api_router.include_router(analysis.router, prefix="/analysis", tags=["EDA"])
api_router.include_router(ml.router, prefix="/ml", tags=["Machine Learning"])

__all__ = ["api_router"]
