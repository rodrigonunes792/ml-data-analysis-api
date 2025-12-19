import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix
import joblib
import os
from typing import Dict, Any, Tuple

class MLService:
    def __init__(self):
        self.models = {}
        self.models_dir = "trained_models"
        os.makedirs(self.models_dir, exist_ok=True)

    def train_model(self, 
                   df: pd.DataFrame, 
                   target: str, 
                   features: list, 
                   model_type: str = "classification",
                   test_size: float = 0.2) -> Dict[str, Any]:
        
        X = df[features]
        y = df[target]

        # Handle missing values simply for this demo
        X = X.fillna(0)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

        model = None
        metrics = {}

        if model_type == "classification":
            model = RandomForestClassifier(n_estimators=100)
            model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = model.predict(X_test)
            metrics = {
                "accuracy": accuracy_score(y_test, y_pred),
                "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
            }
            
        elif model_type == "regression":
            model = RandomForestRegressor(n_estimators=100)
            model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = model.predict(X_test)
            metrics = {
                "mse": mean_squared_error(y_test, y_pred),
                "r2_score": r2_score(y_test, y_pred)
            }
        else:
            raise ValueError("Unsupported model type")

        # Save model
        model_id = f"model_{len(self.models) + 1}"
        self.models[model_id] = {
            "model": model,
            "features": features,
            "type": model_type,
            "metrics": metrics
        }
        
        # Persist model
        joblib.dump(model, os.path.join(self.models_dir, f"{model_id}.joblib"))

        return {
            "model_id": model_id,
            "metrics": metrics
        }

    def predict(self, model_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        if model_id not in self.models:
            # Try loading from disk
            model_path = os.path.join(self.models_dir, f"{model_id}.joblib")
            if os.path.exists(model_path):
                # This is a simplified loading - in real app we'd need metadata
                pass 
            raise ValueError(f"Model {model_id} not found")

        model_info = self.models[model_id]
        model = model_info["model"]
        features = model_info["features"]

        # Prepare input
        input_data = pd.DataFrame([data])
        # Ensure all columns exist and order matches
        for f in features:
            if f not in input_data.columns:
                input_data[f] = 0
        
        X_pred = input_data[features]
        
        prediction = model.predict(X_pred)[0]
        
        result = {"prediction": float(prediction) if isinstance(prediction, (np.float32, np.float64)) else int(prediction)}
        
        if model_info["type"] == "classification" and hasattr(model, "predict_proba"):
            probs = model.predict_proba(X_pred)[0]
            result["probability"] = float(max(probs))

        return result
