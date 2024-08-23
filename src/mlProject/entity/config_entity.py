from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    """l1_ration, alpha => will be define in params.yaml as there are parameters
    in params.yaml => we can set params random forest, linear regression, decision tree etc...
    target will be get from schema.yaml
    """
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: Path
    alpha: float
    l1_ratio: float
    target_column: str