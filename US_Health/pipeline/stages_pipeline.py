from US_Health.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        data_ingestion = DataIngestion()
        data_ingestion.download_file()
        data_ingestion.unzip_operation()