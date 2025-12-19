from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import Dict, Any
import pandas as pd
import io
from app.services.eda_service import EDAService
from app.models.schemas import DatasetInfo

router = APIRouter()
eda_service = EDAService()

# In-memory storage for uploaded dataframes (in production use Redis/S3/DB)
datasets = {}

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")
    
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        
        dataset_id = str(len(datasets) + 1)
        datasets[dataset_id] = df
        
        analysis = eda_service.analyze_dataset(df)
        
        return {
            "message": "Dataset uploaded successfully",
            "dataset_id": dataset_id,
            "analysis": analysis
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{dataset_id}/summary")
async def get_summary(dataset_id: str):
    if dataset_id not in datasets:
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    df = datasets[dataset_id]
    return eda_service.analyze_dataset(df)

@router.get("/{dataset_id}/histogram/{column}")
async def get_histogram(dataset_id: str, column: str):
    if dataset_id not in datasets:
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    df = datasets[dataset_id]
    try:
        return eda_service.generate_histogram(df, column)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
