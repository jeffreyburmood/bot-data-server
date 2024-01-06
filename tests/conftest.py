""" this file contains the various fixture methods used by the pytest framework """

import logging

from _pytest.fixtures import fixture


@fixture(scope="session")
def init_logger() -> logging.Logger:
    """ this method will initialize each tests case to use the pytest logger when logging tests messages  """
    return logging.getLogger("testLogger")
