from pathlib import Path

# Resolve project root: src/my_project/constants/__init__.py → src → END_TO_END_ML_PROJECT
ROOT_DIR = Path(__file__).resolve().parents[3]

# Absolute paths for configuration files
CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"
SCHEMA_FILE_PATH = ROOT_DIR / "schema.yaml"
