import sys
from shipment.exception import shippingException
import logging
# Initializing logger
logger = logging.getLogger(__name__)

from shipment.configuration.mongo_operations import MongoDBOperation
from shipment.entity.artifacts_entity import (
    DataIngestionArtifacts,DataValidationArtifacts,
)
from shipment.entity.config_entity import (
    DataIngestionConfig,DataValidationConfig,
    )

from shipment.components.data_ingestion import DataIngestion
from shipment.components.data_validation import DataValidation

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.mongo_op = MongoDBOperation()

    # This method is used to start the data ingestion
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logger.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logger.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config, mongo_op=self.mongo_op
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logger.info("Got the train_set and test_set from mongodb")
            logger.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact

        except Exception as e:
            raise shippingException(e, sys) from e
        


    # This method is used to start the data validation
    def start_data_validation(
        self, data_ingestion_artifact: DataIngestionArtifacts
    ) -> DataValidationArtifacts:
        logger.info("Entered the start_data_validation method of TrainPipeline class")
        try:
            data_validation = DataValidation(
                data_ingestion_artifacts=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            logger.info("Performed the data validation operation")
            logger.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )
            return data_validation_artifact

        except Exception as e:
            raise shippingException(e, sys) from e
        
#this method is use to start the training pipeline
    def run_pipeline(self) -> None:
        logger.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            self.data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
            )

            logger.info("Exited the run_pipeline method of TrainPipeline class")
            
        except Exception as e:
            raise shippingException(e, sys) from e