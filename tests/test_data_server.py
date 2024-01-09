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

def test_get_transactions(init_logger):
    logger = init_logger

    __name__ = 'test_get_transactions'
    logger.info(f'running {__name__} test case')

    try:
        response = requests.get("http://127.0.0.1:8080/transactions")

        assert response.status_code == 200
        logger.debug("received expected status code")

        response_body = response.json()
        assert len(response_body) > 0
        for entry in response_body.keys():
            headings = response_body[entry]
            assert "time" in headings
            assert "order_type" in headings
            assert "status" in headings
            assert "spend" in headings
            assert "spend_currency" in headings
            assert "received" in headings
            assert "received_currency" in headings
            assert "fee" in headings
            assert "unit_price" in headings

        logger.debug("received expected API response")

    except AssertionError as ae:
        logger.error(f'assert exception found in {__name__}, looks like {ae}')
        assert False

    except Exception as ex:
        logger.error(f"exception encounter in {__name__}, looks like {ex}")
        assert False

def test_get_a_transaction(init_logger):
    logger = init_logger

    __name__ = 'test_get_a_transaction'
    logger.info(f'running {__name__} test case')

    try:
        response = requests.get("http://127.0.0.1:8080/transactions/1")

        assert response.status_code == 200
        logger.debug("received expected status code")

        response_body = response.json()
        assert len(response_body) == 9
        headings = response_body.keys()
        assert "time" in headings
        assert "order_type" in headings
        assert "status" in headings
        assert "spend" in headings
        assert "spend_currency" in headings
        assert "received" in headings
        assert "received_currency" in headings
        assert "fee" in headings
        assert "unit_price" in headings

        logger.debug("received expected API response")

    except AssertionError as ae:
        logger.error(f'assert exception found in {__name__}, looks like {ae}')
        assert False

    except Exception as ex:
        logger.error(f"exception encounter in {__name__}, looks like {ex}")
        assert False