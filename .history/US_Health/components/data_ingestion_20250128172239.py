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
        if not os.path.exists(self.data_ingestion.local_data_path):
            urlretrieve(self.data_ingestion.URL,self.data_ingestion.local_data_path)
            logging.info("file download completed")
            
        else:
            logging.info("file already exists")
            
    def unzip_operation(self):
        with zipfile.ZipFile(self.data_ingestion.local_data_path) as f:
            f.extractall(self.data_ingestion.unzip_dir)
            logging.info("Data unzip completed")                
        
        