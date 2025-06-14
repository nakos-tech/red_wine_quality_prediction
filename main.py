from src.my_project import logger
from src.my_project.pipeline.stage_1_data_ingestion import DataIngrestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

if __name__ == "__main__":
    try:
        logger.info(f">> stage {STAGE_NAME} has started >>>>")
        obj = DataIngrestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed >>>>>")

    except Exception as e:
        logger.exception(e)
        raise e 