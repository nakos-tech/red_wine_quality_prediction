from src.my_project import *
from src.my_project.utils.common import read_yml, create_directories, save_json, load_json
from src.my_project.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from pathlib import Path
from pathlib import Path

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