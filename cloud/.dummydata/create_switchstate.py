from pymongo import MongoClient
import datetime

class MongoDBMgmt:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['SecurityDB']
        self.collection_switchstate = self.db['SwitchState']

    def insert_switchstate(self):
        curtime = datetime.datetime.now().strftime("%Y%m%d%H%M")
        self.collection_switchstate.insert_one({
        "uniqueid": "7712345678902",
         "timestamp": curtime,
         "pv_supply": "ON",
         "bat_supply": "OFF",
         "bat_charge": "OFF",
         "ev_charge": "OFF",
         "appl_supply": "ON",
         "grid_supply": "OFF",
         "grid_dump": "OFF"})

        self.collection_switchstate.insert_one({
        "uniqueid": "7712345678903",
        "timestamp": curtime,
        "pv_supply": "ON",
        "bat_supply": "OFF",
        "bat_charge": "ON",
        "ev_charge": "OFF",
        "appl_supply": "ON",
        "grid_supply": "OFF",
        "grid_dump": "OFF"})


if __name__ == '__main__':
    dummydata = MongoDBMgmt()
    dummydata.collection_switchstate.drop()
    dummydata.insert_switchstate()