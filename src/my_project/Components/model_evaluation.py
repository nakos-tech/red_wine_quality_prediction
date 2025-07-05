import os
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from urllib.parse import urlparse
import numpy as np
import joblib
from pathlib import Path
from src.my_project.entity.config_entity import ModelEvaluationConfig
from src.my_project.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config 

    def eval_metrics(self, actual, predicted):
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)

        return rmse, mae, r2

    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop(columns=[self.config.target_column])
        y_test = test_data[self.config.target_column]

        predicted_values = model.predict(X_test)

        rmse, mae, r2 = self.eval_metrics(y_test, predicted_values)

        metrics = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        save_json(path=Path(self.config.metric_file_name), data=metrics)
