import pandas as pd
import numpy as np
from typing import Dict, Any, List
from io import StringIO
import json

class EDAService:
    @staticmethod
    def analyze_dataset(df: pd.DataFrame) -> Dict[str, Any]:
        """
        Perform comprehensive exploratory data analysis on a pandas DataFrame
        """
        # Basic Info
        info = {
            "rows": len(df),
            "columns": len(df.columns),
            "memory_usage": df.memory_usage(deep=True).sum(),
            "missing_cells": df.isnull().sum().sum(),
            "missing_cells_pct": (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
        }

        # Column Analysis
        columns = []
        for col in df.columns:
            col_data = {
                "name": col,
                "dtype": str(df[col].dtype),
                "missing": int(df[col].isnull().sum()),
                "unique": int(df[col].nunique())
            }
            
            # Numerical Stats
            if pd.api.types.is_numeric_dtype(df[col]):
                col_data.update({
                    "mean": float(df[col].mean()),
                    "std": float(df[col].std()),
                    "min": float(df[col].min()),
                    "max": float(df[col].max()),
                    "median": float(df[col].median())
                })
            
            columns.append(col_data)

        # Correlation Matrix (for numerical columns)
        numeric_df = df.select_dtypes(include=[np.number])
        correlation = None
        if not numeric_df.empty and len(numeric_df.columns) > 1:
            corr_matrix = numeric_df.corr().round(2)
            correlation = corr_matrix.to_dict()

        return {
            "info": info,
            "columns": columns,
            "correlation": correlation
        }

    @staticmethod
    def generate_histogram(df: pd.DataFrame, column: str) -> Dict[str, Any]:
        """Generate data for a histogram"""
        if column not in df.columns:
            raise ValueError(f"Column {column} not found")
        
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"Column {column} is not numeric")

        counts, bins = np.histogram(df[column].dropna(), bins='auto')
        return {
            "type": "histogram",
            "column": column,
            "bins": bins.tolist(),
            "counts": counts.tolist()
        }
