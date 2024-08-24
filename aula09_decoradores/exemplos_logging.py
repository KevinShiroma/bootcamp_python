from loguru import logger

logger.debug("Um aviso para o dev (ou eu mesmo no futuro")
logger.info("Info importante do processo")
logger.warning("Um aviso de que algo no futuro vai parar de funcionar")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu um que aborta a aplicação")