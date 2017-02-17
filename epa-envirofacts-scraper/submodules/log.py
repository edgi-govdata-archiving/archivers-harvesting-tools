import logging

logging.getLogger("requests").setLevel(logging.WARNING)

def initLogger(name, level=logging.INFO, format=None):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logging.basicConfig(
        level=level,
        format=format if format else
        "%(levelname)s %(asctime)-15s %(filename)s(%(lineno)d) %(message)s")

    return logger
