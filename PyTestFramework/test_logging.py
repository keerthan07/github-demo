import logging


def test_logging_demo():

    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)

    logger.debug("Debug log details")
    logger.info("Information")
    logger.warning("A simple warning")
    logger.error("An error occured while executing the step")
    logger.critical("A critical issue")
