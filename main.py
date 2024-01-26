# print("It's a practice end-to-end automation framework")
import logging


def log():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S %p',
                        filename=".\\Logs\\automation.log",
                        )
    return logging.getLogger()


logger = log()
logger.info("This is an info message.")
logger.debug("This is a debug message.")



