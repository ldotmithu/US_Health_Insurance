from US_Health.config_entity import DataTransfomationConfig
from sklearn.model_selection import train_test_split
import pandas as pd 
from US_Health.utility.comon import create_folder
from US_Health import logging
import os 

class DataTransfomation:
    def __init__(self):
        self.data_transfomation = DataTransfomationConfig()
        
        create_folder(self.data_transfomation.root_dir)
        
    def split_data(self):
        data = pd.read_csv(self.data_transfomation.data_path)
        logging.info('Read the data through Panda DF')
        
        train_data,test_data = train_test_split(data,test_size=0.2,random_state=12)
        logging.info('Split the Data into Train and Test')
        
        train_data.to_csv(os.path.join(self.data_transfomation.root_dir,"train.csv"),index=False)
        
        test_data.to_csv(os.path.join(self.data_transfomation.root_dir,"test.csv"),index=False)
           