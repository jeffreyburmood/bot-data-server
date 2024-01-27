""" this file contains practice code for reading in CSV file data """

import csv

column_names = ["time", "order_type", "status", "spend", "spend_currency", "received", "received_currency", "fee", "unit_price"]

with open("TransactionHistory.csv") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=column_names)

    print(type(reader))
    for row in reader:
        print(type(row))
        print(row)