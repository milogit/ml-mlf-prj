from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

#logger.info("Welcome to custom log")

STAGE_NAME = "Data Ingestion stage"
try :
    logger.info(f">>>>> stage {STAGE_NAME} starte <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e
