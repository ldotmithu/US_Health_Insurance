from US_Health.pipeline.stages_pipeline import DataIngestionPipeline,DataTransfomationPipeline,ModelTrainPipeline,ModelEvaluationPipeline
import logging
from US_Health import logging 

try:
    logging.info('>>>>>DataIngestion>>>>>>>')
    data_ingestion=DataIngestionPipeline()
    data_ingestion.Main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e 

try:
    logging.info('>>>>>DataTransform>>>>>>>')
    data_transfomation=DataTransfomationPipeline()
    data_transfomation.Main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e 

try:
    logging.info('>>>>>ModelTrain>>>>>>>')
    model_train=ModelTrainPipeline()
    model_train.Main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e 