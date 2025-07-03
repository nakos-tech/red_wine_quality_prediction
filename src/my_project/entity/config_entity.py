from dataclasses import dataclass
from pathlib import Path
import os
import pandas as pd

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_dir: Path
    all_schema: dict

BASE_DIR = os.getcwd() 

file_path = os.path.join(BASE_DIR, "artifacts", "data_ingestion", "winequality-red.csv")

# check
print(file_path)

# read
data = pd.read_csv(file_path)
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str


# # Creating an instance of the dataclass
# d = DataValidationConfig(
#     root_dir=Path("artifacts"),
#     STATUS_FILE="True",
#     unzip_dir=Path("artifacts/gt"),
#     all_schema={
#         'artifacts_root': 'artifacts/',
#         'data_validation': {
#             'root_dir': 'artifacts/data_validation',
#             'STATUS_FILE': 'status.txt',
#             'unzip_dir': 'artifacts/data_ingestion/unzip'
#         }
#     }
# )

# # Print the correct attribute
# print(d.root_dir)
