""" this file contains the test cases for the bot data server code """

import pytest
import requests

####################### transaction history API routes test cases ####################

def test_get_root(init_logger):
    logger = init_logger

    __name__ = 'test_get_root'
    logger.info(f'running {__name__} test case')

    try:
        response = requests.get("http://127.0.0.1:8080")

        assert response.status_code == 200
        logger.debug("received expected status code")

        assert response.json() == "Welcome to the Transaction Data Server!!!"
        logger.debug("received expected API response")

    except AssertionError as ae:
        logger.error(f'assert exception found in {__name__}, looks like {ae}')
        assert False

    except Exception as ex:
        logger.error(f"exception encounter in {__name__}, looks like {ex}")
        assert False