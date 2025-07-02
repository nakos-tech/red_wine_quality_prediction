import os 
import urllib.request as request
import zipfile
from src.my_project import logger
from src.my_project.utils.common import get_size
from pathlib import Path
import pandas as pd
from src.my_project.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def training_test_split(self):
        print("Current working directory:", os.getcwd())
        print("Configured data path:", self.config.data_path)
        print("Does the file exist?", Path(self.config.data_path).exists())
        print("Absolute path:", Path(self.config.data_path).resolve())

        data = pd.read_csv(self.config.data_path) 

        train, test = train_test_split(data)

        self.config.root_dir.mkdir(parents=True, exist_ok=True)

        train_path = self.config.root_dir / "train.csv"
        test_path = self.config.root_dir / "test.csv"

        train.to_csv(train_path, index=False)
        test.to_csv(test_path, index=False)
        logger.info("splitted data into training and testing sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
