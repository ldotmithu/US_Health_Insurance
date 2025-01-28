from US_Health.pipeline.stages_pipeline import DataIngestionPipeline
import logging
from US_Health import logging 

try:
    logging.info('>>>>>DataIngestion>>>>>>>')
    data_ingestion=DataIngestionPipeline()
    data_ingestion.Main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e 