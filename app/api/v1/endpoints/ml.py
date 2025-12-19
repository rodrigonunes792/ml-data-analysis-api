from fastapi import APIRouter, HTTPException
from app.models.schemas import ModelTrainRequest, ModelMetrics, PredictionRequest, PredictionResponse
from app.services.ml_service import MLService
from app.api.v1.endpoints.analysis import datasets

router = APIRouter()
ml_service = MLService()

@router.post("/{dataset_id}/train", response_model=Dict[str, Any])
async def train_model(dataset_id: str, request: ModelTrainRequest):
    if dataset_id not in datasets:
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    df = datasets[dataset_id]
    
    # Validation
    if request.target_column not in df.columns:
        raise HTTPException(status_code=400, detail=f"Target column {request.target_column} not found")
    
    for feature in request.feature_columns:
        if feature not in df.columns:
            raise HTTPException(status_code=400, detail=f"Feature column {feature} not found")

    try:
        result = ml_service.train_model(
            df, 
            request.target_column, 
            request.feature_columns, 
            request.model_type,
            request.test_size
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict/{model_id}", response_model=PredictionResponse)
async def predict(model_id: str, request: PredictionRequest):
    try:
        result = ml_service.predict(model_id, request.features)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
