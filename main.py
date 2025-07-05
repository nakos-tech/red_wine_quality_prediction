from src.my_project import logger
from src.my_project.pipeline.ingestion_stage import DataIngrestionTrainingPipeline
from src.my_project.pipeline.validation_stage import DataValidationTrainingPipeline
from src.my_project.pipeline.transformation_stage import DataTransformationTrainingPipeline
from src.my_project.pipeline.model_training_stage import ModelTrainingPipeline
from src.my_project.pipeline.model_evaluation_stage import ModelEvaluationPipeline

if __name__ == "__main__":
    try:
        STAGE_NAME = "Data Ingestion stage"
        logger.info(f">> stage {STAGE_NAME} has started >>>>")
        obj = DataIngrestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")

        STAGE_NAME = "Data Validation stage"
        logger.info(f">> stage {STAGE_NAME} has started >>>>")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")

        STAGE_NAME = "Data Transformation stage"
        logger.info(f">> stage {STAGE_NAME} has started >>>>")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")

        STAGE_NAME =" model training stage"
        logger.info(f">> stage {STAGE_NAME} has started >>>>")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")

        STAGE_NAME =" model evaluation stage"
        logger.info(f">> stage {STAGE_NAME} has started >>>>")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")


    except Exception as e:
        logger.exception(e)
        raise e
        
