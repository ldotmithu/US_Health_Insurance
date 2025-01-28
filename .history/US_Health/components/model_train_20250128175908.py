from US_Health.config_entity import ModelTrainConfig
import joblib
import pandas as pd 
from sklearn.preprocessing import StandardScaler,OneHotEncoder,PowerTransformer
from sklearn.compose import ColumnTransformer
from US_Health.utility.comon import *
from sklearn.model_selection import train_test_split

class ModelTrain:
    def __init__(self):
        self.model_train =ModelTrainConfig()
        
        create_folder(self.model_train.root_dir)
        
    def preprocess(self):
        
        cat_col = ['sex','smoker','region']
        num_col =['age', 'bmi', 'children']
        power_col='bmi'
        
        perprocess = ColumnTransformer([
        ('num_pipeline',StandardScaler(),num_col),
        ('cat_pipeline',OneHotEncoder(),cat_col),
        'power',PowerTransformer(method='yeo-johnson'),power_col,
        ])
        
        return perprocess
    def after_preprocess(self):
        train_data = pd.read_csv(self.model_train.train_data_path)
        
        train_X =train_data.drop(columns='charges',axis=1)
        train_y = train_data['charges']
        
        preprocess_obj = self.preprocess()
        
        X_train = preprocess_obj.fit_transform(X_train)
        
        
        
        
            