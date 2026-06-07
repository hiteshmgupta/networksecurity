import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)
        
        logging.info("Initiate the data ingestion")

        dataingestionartifact=dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)