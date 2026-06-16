from dataclasses import dataclass

#Data ingestion  Artifacts

@dataclass
class DataIngestionArtifacts:
    train_data_file_path: str
    test_data_file_path: str 


#Data validation atifacts 

@dataclass
class DataValidationArtifacts:
    data_drift_file_path: str
    validation_status:  bool


#Data transformation artifacts

@dataclass
class DataTransformationArtifacts:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str