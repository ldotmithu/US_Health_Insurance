from US_Health.config_entity import ModelTrainConfig
import joblib
import pandas as pd 
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from US_Health.utility.comon import *

class ModelTrain:
    def __init__(self):
        self.model_train =ModelTrainConfig()
        
        create_folder(self.model_train.root_dir)
        
    def preprocess(self):
        train_data = pd.read_csv(self.model_train.train_data_path)
            