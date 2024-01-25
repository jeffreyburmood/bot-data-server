""" this file contains the API route functions used for the data server """

import logging
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from transaction_history import Transaction
from connectors import PostgresDB
import psycopg

app = FastAPI()

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

transactions = {
    0: Transaction(time="12/19/2023 4:22:16 PM", order_type="Market Buy", status="Executed",
                   spend=1000.000000000, spend_currency="USD", received=13.315536970000, received_currency="Sol",
                   fee=10.000000000000, unit_price=74.349235951241),
    1: Transaction(time="12/19/2023 4:20:33 PM", order_type="Market Buy", status="Executed",
                   spend=260.000000000000, spend_currency="USD", received=512.540000000000, received_currency="Sand",
                   fee=2.600000000000, unit_price=0.502204705974),
    2: Transaction(time="12/9/2023 11:12:34 AM", order_type="Market Sell", status="Executed",
                   spend=4.000000000000, spend_currency="AVAX", received=133.060000000000, received_currency="Usd",
                   fee=1.352235772358, unit_price=33.600000000000)
}

logger.info(f"transactions built!, type = {type(transactions)}")

# Transaction data server routes
@app.get("/")
def root() -> str:
    __name__ = 'root'
    logger.info(f'received GET request to the {__name__} route')
    return "Welcome to the Transaction Data Server!!!"

@app.get("/transactions/{transaction_id}")
def query_transactions_by_id(transaction_id: int) -> Transaction:
    __name__ = 'query_transactions_by_id'
    logger.info(f'received GET request to the {__name__} route')
    if transaction_id not in transactions:
        raise HTTPException(status_code=404, detail=f"Transaction with id {transaction_id} not found")
    return transactions[transaction_id]

@app.get("/transactions")
def query_transactions() -> dict[int, Transaction]:
    __name__ = 'query_transactions'
    logger.info(f'received GET request to the {__name__} route')
    return transactions

# Postgres DB related routes

@app.get("/postgres/connection-info")
def query_connection_info() -> dict[str: str | int]:
    __name__ = 'query_connection_info'
    logger.info(f'received GET request to the {__name__} route')
    db = PostgresDB()
    with psycopg.connect(conninfo=db.connection_str) as conn:
        connection = db.get_connection_info(conn)
        connection_info = {
            "status": str(connection.status.value),
            "host": connection.host,
            "hostaddr": connection.hostaddr,
            "port": connection.port,
            "dbname": connection.dbname,
            "user": connection.user
        }

    return connection_info
