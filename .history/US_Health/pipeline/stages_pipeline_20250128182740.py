from US_Health.components.data_ingestion import DataIngestion
from US_Health.components.data_transfomation import DataTransfomation
from US_Health.components.model_train import ModelTrain
from US_Health.components.model_evaluation import ModelEvaluation


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        data_ingestion = DataIngestion()
        data_ingestion.download_file()
        data_ingestion.unzip_operation()
        
class DataTransfomationPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        data_transfomation = DataTransfomation()
        data_transfomation.split_data()        
        
class ModelTrainPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        model_train = ModelTrain()
        model_train.after_preprocess()          