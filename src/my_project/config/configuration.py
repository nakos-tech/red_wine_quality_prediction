from src.my_project import *
from src.my_project.utils.common import read_yml, create_directories, save_json, load_json
from src.my_project.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainingConfig, ModelEvaluationConfig 
from pathlib import Path
from pathlib import Path
from src.my_project.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH


BASE_DIR = Path.cwd()


# Define constants or import them
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")
create_directories([Path("artifacts")])

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH):

        self.config = read_yml(config_filepath)
        self.params = read_yml(params_filepath)
        self.schema = read_yml(schema_filepath)

        # ✅ Wrap in Path and in a list
        create_directories([Path(self.config.artifacts_root)])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([Path(config.root_dir)])

        data_download = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_download


class ValidationConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH):

        self.config = read_yml(config_filepath)
        self.params = read_yml(params_filepath)
        self.schema = read_yml(schema_filepath)

        create_directories([self.config['artifacts_root']])
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config['data_validation']
        schema = self.schema['COLUMNS']
        create_directories([config['root_dir']])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config['root_dir']),
            STATUS_FILE=config['STATUS_FILE'],
            unzip_dir=Path(config['unzip_dir']),
            all_schema=schema,
        )

        return data_validation_config

class TransformationConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH):

        self.config = read_yml(config_filepath)
        self.params = read_yml(params_filepath)
        self.schema = read_yml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])
        root_dir = Path.cwd() / "artifacts" / "data_transformation"
        file_path = Path.cwd() / "artifacts" / "data_ingestion" / "winequality-red.csv"

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(BASE_DIR) / "artifacts" / "data_transformation",
            data_path=Path(file_path)
            )
        return data_transformation_config


class TrainingConfigurationManager():
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yml(config_filepath)
        self.params = read_yml(params_filepath)
        self.schema = read_yml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.ElasticNet
        schema = self.schema.TARGET

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )


        return model_training_config

class EvaluationConfigurationManager:
   
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH):

        self.config = read_yml(config_filepath)
        self.params = read_yml(params_filepath)
        self.schema = read_yml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET

        create_directories([self.config.model_evaluation.root_dir])  # ✅


        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path= config.model_path,
            all_params=params,
            metric_file_name= config.metric_file_name,
            target_column = schema.name 
        )

        return model_evaluation_config