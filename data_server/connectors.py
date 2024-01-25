""" this file contains the methods used to connect and communicate with the various databases """
import psycopg
from psycopg import ConnectionInfo
import logging

class PostgresDB:

    def __init__(self):
        self.connection_str = "host=172.18.0.2 port=5432 dbname=postgres user=postgres password=ascinc"
        self.logger = logging.Logger

    def get_connection_info(self, conn) -> ConnectionInfo:

        return conn.info

    def write_transaction_history(self):
        # connect to the postgres DB
        with psycopg.connect(conninfo=self.connection_str) as conn:
            return

