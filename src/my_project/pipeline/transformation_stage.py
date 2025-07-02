from src.my_project.config.configuration import TransformationConfigurationManager
from src.my_project.Components.data_transformation import DataTransformation
from src.my_project import logger

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = TransformationConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.training_test_split()


if __name__ == "__main__":
        try:
            logger.info(f">> stage {STAGE_NAME} has started >>>>")
            obj = DataIngrestionTrainingPipeline()
            obj.main()
            logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")

        except Exception as e:
            logger.exception(e)
            raise e