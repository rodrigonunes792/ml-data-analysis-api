from pydantic import BaseModel
from typing import List, Optional, Dict, Any

# Dataset Schemas
class DatasetInfo(BaseModel):
    filename: str
    rows: int
    columns: int
    missing_values: Dict[str, int]
    dtypes: Dict[str, str]

class ColumnStats(BaseModel):
    name: str
    dtype: str
    count: int
    mean: Optional[float] = None
    std: Optional[float] = None
    min: Optional[float] = None
    max: Optional[float] = None
    unique_values: int

# ML Model Schemas
class ModelTrainRequest(BaseModel):
    target_column: str
    feature_columns: List[str]
    model_type: str = "classification"  # or "regression"
    test_size: float = 0.2

class ModelMetrics(BaseModel):
    accuracy: Optional[float] = None
    mse: Optional[float] = None
    r2_score: Optional[float] = None
    confusion_matrix: Optional[List[List[int]]] = None

class PredictionRequest(BaseModel):
    features: Dict[str, Any]

class PredictionResponse(BaseModel):
    prediction: Any
    probability: Optional[float] = None
