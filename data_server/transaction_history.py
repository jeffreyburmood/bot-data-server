""" this file contains the data model and data server for the trading transaction history """

import logging
from typing import Any

from pydantic import BaseModel

class Transaction(BaseModel):
    time: str
    order_type: str
    status: str
    spend: float
    spend_currency: str
    received: float
    received_currency: str
    fee: float
    unit_price: float

    def __init__(self, **data: Any):
        super().__init__(**data)



