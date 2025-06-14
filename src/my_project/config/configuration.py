from src.my_project import *
from src.my_project.utils.common import read_yml, create_directories, save_json, load_json
from src.my_project.entity.config_entity import DataIngestionConfig
from pathlib import Path

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
