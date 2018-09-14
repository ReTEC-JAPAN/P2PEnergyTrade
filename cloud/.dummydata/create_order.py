#!flask/bin/python
from pymongo import MongoClient
import datetime
import time



class MongoDBMgmt:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['SecurityDB']
        self.collection_orders = self.db['Orders']

    def insert_orders(self):
        curtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        orderid = "ORD" + curtime
        self.collection_orders.insert_one({'orderid': orderid, 'userid': 'bmohanty',
                                           'uniqueid': "7712345678902",
                                           'timestamp': curtime,
                                           'type': "B",
                                           'qty': 10,
                                           'unitrate': 20,
                                           'status': "O",  # Order is OPEN, C -> Contracted, F -> Fulfilled
                                           'contractid': ""})
        time.sleep(2)
        curtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        orderid = "ORD" + curtime
        self.collection_orders.insert_one({'orderid': orderid, 'userid': 'gdooley',
                                           'uniqueid': "7712345678903",
                                           'timestamp': curtime,
                                           'type': "S",
                                           'qty': 10,
                                           'unitrate': 20,
                                           'status': "O",  # Order is OPEN, C -> Contracted, F -> Fulfilled
                                           'contractid': ""})

if __name__ == '__main__':
    dummydata = MongoDBMgmt()
    dummydata.collection_orders.drop()
    dummydata.insert_orders()
 #   dummydata.insert_statelog()