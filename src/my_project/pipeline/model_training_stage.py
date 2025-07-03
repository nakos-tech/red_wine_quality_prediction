from src.my_project.config.configuration import TrainingConfigurationManager
from src.my_project.Components.model_training import ModelTraining
from src.my_project import logger

STAGE_NAME = "model training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = TrainingConfigurationManager()
        training_config = config.get_training_config()
        training_config = ModelTraining(config=training_config)
        training_config.train()


if __name__ == "__main__":
    try:
        logger.info(f">> stage {STAGE_NAME} has started >>>>")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")

    except Exception as e:
        logger.exception(e)
        raise e