from src.my_project.config.configuration import EvaluationConfigurationManager
from src.my_project.Components.model_evaluation import ModelEvaluation
from src.my_project import logger


STAGE_NAME = "model evaluation stage"

class ModelEvaluationPipeline:

    def __init__(self):
        pass 

    def main(self):
        config = EvaluationConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()

if __name__ == "__main__":
    try:
        logger.info(f">> stage {STAGE_NAME} has started >>>>")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")

    except Exception as e:
        logger.exception(e)
        raise e
