from pathlib import Path
import os 
from dataclasses import dataclass

@dataclass 
class DataIngestionConfig:
    root_dir:Path="artifacts/data_ingestion"
    URL:str="https://github.com/ldotmithu/Dataset/raw/refs/heads/main/US_Health.zip"
    local_data_path:Path="artifacts/data_ingestion/data.zip"
    unzip_dir:Path="artifacts/data_ingestion"
    
@dataclass
class DataTransfomationConfig:
    root_dir:Path="artifacts/data_transforam"
    data_path:Path="artifacts\data_ingestion\insurance.csv"   
    
    
@dataclass
class ModelTrainConfig:
    root_dir:Path="artifacts/model_train"
    train_data_path:Path="artifacts/data_transforam/train.csv"
    model_name:str="model.json"
    preprocess_name:str="preprocess.pkl"
    
@dataclass
class ModelEvaluationConfig:
    root_dir:Path="artifacts/model_evaluation"
    test_data_path:Path="artifacts/data_transforam/test.csv"
    preprocess_path:Path="artifacts\model_train\preprocess.pkl"
    model_Path:Path="artifacts\model_train\model.pkl"   
    metrics:Path="artifacts\model_train\metrics"
    
    
         
    