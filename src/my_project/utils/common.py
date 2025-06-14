import os
from box.exceptions import BoxValueError 
import yaml
from src.my_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any 

# logger = logging.getLogger(__name__)
@ensure_annotations
def read_yml(path_to_yml: Path) -> ConfigBox:
    try:
        with open(path_to_yml) as yml_file:
            content = yaml.safe_load(yml_file)
            logger.info(f"YML file: {path_to_yml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories.

    Args:
        path_to_directories (list): List of directory paths.
        verbose (bool): Whether to log creation info.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):

    """
    save json data

    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:

    """
    load json files data

    """

    with open(path) as f:
        content = json.load(f)
        logger.info(f"json file loaded successfuly from: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary data

    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")

    return data 

@ensure_annotations 
def get_size(path: Path) -> str:
    """
    get size in kb

    """ 
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

      