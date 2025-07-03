import pandas as pd
import os
import joblib 
from sklearn.linear_model import ElasticNet
import joblib
from src.my_project.entity.config_entity import ModelTrainingConfig  
from pathlib import Path
from src.my_project import logger

class ModelTraining:
    def __init__(self, config:ModelTrainingConfig):
        self.config = config

    def train(self):
        print("Train data path from config:", self.config.train_data_path)
        print("Resolved path:", Path(self.config.train_data_path).resolve())
        print("Exists:", Path(self.config.train_data_path).exists())

        training_data = pd.read_csv(self.config.train_data_path)
        testing_data = pd.read_csv(self.config.test_data_path)
        
        X_train = training_data.drop(columns=[self.config.target_column])
        y_train = training_data[self.config.target_column]
        X_test = testing_data.drop(columns=[self.config.target_column])
        y_test = testing_data[self.config.target_column]

        lr = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )
        lr.fit(X_train, y_train)
        joblib.dump(lr,os.path.join(self.config.root_dir, self.config.model_name))

        
        logger.info(f"Model trained and saved at {self.config.root_dir / self.config.model_name}")
        