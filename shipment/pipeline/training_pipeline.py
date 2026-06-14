import sys
from shipment.exception import shippingException
import logging
# Initializing logger
logger = logging.getLogger(__name__)

from shipment.configuration.mongo_operations import MongoDBOperation
from shipment.entity.artifacts_entity import (
    DataIngestionArtifacts
)
from shipment.entity.config_entity import (
    DataIngestionConfig
    )

from shipment.components.data_ingestion import DataIngestion


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
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
        

    def run_pipeline(self) -> None:
        logger.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifact = self.start_data_ingestion()

            logger.info("Exited the run_pipeline method of TrainPipeline class")
            
        except Exception as e:
            raise shippingException(e, sys) from e    