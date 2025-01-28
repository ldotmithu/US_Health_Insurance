from US_Health.utility.comon import *
import os,joblib
import pandas as pd 
from sklearn.model_selection import train_test_split
from US_Health.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self):
        self.model_evaluation = ModelEvaluationConfig()
        
        create_folder(self.model_evaluation.root_dir)
        
    def Predit_model_to_Test_data(self):
        test_data = pd.read_csv(self.model_evaluation.test_data_path)
        
        test_X = test_data.drop(columns=['charges'],axis=1) 
        test_y = test_data['charges']  
        
        preprocess_obj = joblib.load(self.model_evaluation.preprocess_path)
        model = joblib.load(self.model_evaluation.model_Path)
        
        test_X = preprocess_obj.transform(test_X)
        model.