import logging


FORMAT = '[%(name)s] %(levelname)s:%(message)s'
FORMATTER = logging.Formatter(fmt=FORMAT)


def get_logger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler()
    handler.setFormatter(fmt=FORMATTER)
    logger.addHandler(handler)

    return logger
