from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import datetime



class MongoDBMgmt:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['SecurityDB']
        self.collection_configs = self.db['Configs']

    def insert_configs(self):
        self.collection_configs.insert_one({
            "uniqueid" : "7712345678903",
            "timestamp" : "201808250749",
            "synchstatus" : "S",
            "pv" : "Y",
            "pv_cap" : "50",
            "pv_desc" : "25 x 2Kw Kyocera Panels, 80 percent Efficiency",
            "bat" : "Y",
            "bat_cap" : "120",
            "bms_desc" : "120kwh Li Ion Battery",
            "ev" : "N",
            "ev_cap" : "0",
            "ev_desc" : "Does not exist",
            "appl" : "Y",
            "appl_cap" : "6.6",
            "appl_desc" : "House hold appliance with 60A Circuit Breaker at 110V" })

        self.collection_configs.insert_one({
            "uniqueid" : "7712345678902",
            "timestamp" : "201808250749",
            "synchstatus" : "S",
            "pv" : "Y",
            "pv_cap" : "5",
            "pv_desc" : "5 x 1Kw Kyocera Panels, 80 percent Efficiency",
            "bat" : "N",
            "bat_cap" : "0",
            "bms_desc" : "Does not exist",
            "ev" : "N",
            "ev_cap" : "0",
            "ev_desc" : "Does not exist",
            "appl" : "Y",
            "appl_cap" : "6.6",
            "appl_desc" : "House hold appliance with 60A Circuit Breaker at 110V" })

        self.collection_configs.insert_one({
            "uniqueid" : "7712345678901",
            "timestamp" : "201808250758",
            "synchstatus" : "S",
            "pv" : "Y",
            "pv_cap" : "10",
            "pv_desc" : "5 x 2Kw Kyocera Panels, 80 percent Efficiency",
            "bat" : "Y",
            "bat_cap" : "200",
            "bms_desc" : "200kwh Li Ion Battery",
            "ev" : "N",
            "ev_cap" : "0",
            "ev_desc" : "Does not exist",
            "appl" : "Y",
            "appl_cap" : "6.6",
            "appl_desc" : "House hold appliance with 60A Circuit Breaker at 110V" })

if __name__ == '__main__':
    dummydata = MongoDBMgmt()

    dummydata.collection_configs.drop()
    dummydata.insert_configs()
