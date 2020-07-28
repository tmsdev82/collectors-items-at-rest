import sys
import os
import logging

def get_basic_logger(name):
    """ Returns a logging object that logs to std out. """
    basic_formatter = logging.Formatter(
        "%(asctime)s %(module)s %(funcName)s() %(levelname)s: %(message)s"
    )
    logger = logging.getLogger("{}_logger".format(name))
    if os.getenv("LOGGING_LEVEL") == "INFO":
        loglevel = logging.INFO
    elif os.getenv("LOGGING_LEVEL") == "ERROR":
        loglevel = logging.ERROR
    else:
        loglevel = logging.DEBUG

    logger.setLevel(loglevel)

    std_out_log_handler = logging.StreamHandler(sys.stdout)
    std_out_log_handler.setFormatter(basic_formatter)

    logger.addHandler(std_out_log_handler)
    return logger

