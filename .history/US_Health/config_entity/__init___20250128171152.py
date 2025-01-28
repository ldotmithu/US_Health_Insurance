from pathlib import Path
import os 
from dataclasses import dataclass

@dataclass 
class DataIngestionConfig:
    root_dir:Path="artifacts/dataingestion"
    URL:str=""