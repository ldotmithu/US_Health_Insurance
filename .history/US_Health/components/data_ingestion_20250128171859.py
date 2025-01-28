from US_Health.config_entity import *
from urllib.request import urlretrieve
import zipfile,os 
from US_Health import logging
from US_Health.utility.comon import create_folder

class DataIngestion:
    def __init__(self):
        self.data_ingestion = DataIngestionConfig()
        
        create_folder(self.data_ingestion.root_dir)
        
    def download_file(self):
            
        
        