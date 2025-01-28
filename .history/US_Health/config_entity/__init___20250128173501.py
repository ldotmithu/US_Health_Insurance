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
    