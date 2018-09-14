from flask import Flask
from flask_pymongo import PyMongo
import datetime
import time

app = Flask(__name__)
mongosecurity = PyMongo(app,uri="mongodb://localhost:27017/SecurityDB")
mongodatacollector = PyMongo(app,uri="mongodb://localhost:27017/CollectorDB")


if __name__ == '__main__':
    buy_orders = mongosecurity.db.Orders.find({'type': 'B', 'status': 'O'})
    sale_orders = mongosecurity.db.Orders.find({'type': 'S', 'status': 'O'})
    for buy_order in buy_orders:
        print(buy_order)
        print(buy_order['uniqueid'])
    for sale_order in sale_orders:
        print(sale_order)
        print(sale_order['qty'])
        print(float(sale_order['unitrate']))