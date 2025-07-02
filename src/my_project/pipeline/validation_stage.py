from src.my_project.config.configuration import ValidationConfigurationManager
from src.my_project.Components.data_validation import DataValidation
from src.my_project.config.configuration import ConfigurationManager
from src.my_project import logger


STAGE_NAME = "Data validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ValidationConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">> stage {STAGE_NAME} has started >>>>")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")

    except Exception as e:
        logger.exception(e)
        raise e