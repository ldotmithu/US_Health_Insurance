from US_Health.config_entity import ModelTrainConfig
import joblib,os
import pandas as pd 
from sklearn.preprocessing import StandardScaler,OneHotEncoder,PowerTransformer
from sklearn.compose import ColumnTransformer
from US_Health.utility.comon import *
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.pipeline import Pipeline

class ModelTrain:
    def __init__(self):
        self.model_train =ModelTrainConfig()
        
        create_folder(self.model_train.root_dir)
        
    def preprocess(self):
        
        cat_col = ['sex','smoker','region']
        num_col =['age', 'bmi', 'children']
        power_col=['bmi']
        
        transform=Pipeline([
            ('transform_pipeline',PowerTransformer(method='yeo-johnson'))
        ])
        
        perprocess = ColumnTransformer([
        ('num_pipeline',StandardScaler(),num_col),
        ('cat_pipeline',OneHotEncoder(),cat_col),
        'power',transform,power_col,
        ])
        
        return perprocess
    def after_preprocess(self):
        try:
            train_data = pd.read_csv(self.model_train.train_data_path)
            
            train_X =train_data.drop(columns='charges',axis=1)
            train_y = train_data['charges']
            
            preprocess_obj = self.preprocess()
            
            X_train = preprocess_obj.fit_transform(train_X)
            
            xgb=XGBRegressor()
            xgb.fit(train_X,train_y)
            
            joblib.dump(preprocess_obj,os.path.join(self.model_train.root_dir,self.model_train.preprocess_name))
            logging.info('Preprocess Object save successfully')
            
            joblib.dump(xgb,os.path.join(self.model_train.root_dir,self.model_train.model_name))
            logging.info('Train Model save successfully')
        
        except Exception as e:
            raise e        
                
        
        
            