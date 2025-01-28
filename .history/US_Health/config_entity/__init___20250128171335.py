from pathlib import Path
import os 
from dataclasses import dataclass

@dataclass 
class DataIngestionConfig:
    root_dir:Path="artifacts/dataingestion"
    URL:str=""
    local_data_path:Path="artifacts/data_ingestion/data.zip"
    unzip_dir:Path="artifacts/dataingestion"
    