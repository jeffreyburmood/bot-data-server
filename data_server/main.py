""" this file contains the API route functions used for the data server """

import logging


# setup logger and provide name
logger = logging.getLogger("myLogger")

# setup logging level at the logger level
logger.setLevel(logging.DEBUG)

# setup the handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # set the logging level at the handler level

file_handler = logging.FileHandler("logs.log")
file_handler.setLevel(logging.DEBUG)  # set the logging level at the handler level

# create the formatter (same for both handlers in this example
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s")

# add formatter to handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':
    pass