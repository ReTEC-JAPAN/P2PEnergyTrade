#!flask/bin/python
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import datetime



class MongoDBMgmt:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['SecurityDB']
        self.collection_devices = self.db['EcoBoxes']

    def insert_devices(self):
        self.collection_devices.insert_one({
            "srno": "R2018000012345A",
            "address": "4-5, Hanamachi, Iheya, Okinawa, Japan",
            "uniqueid":"7712345678901",
            "macaddress":"",
            "ipaddress":"",
            "status":"P",     # "P" -> Provisioned, "I" -> Installed but Unregistered, "R" -> Registered
            "authcode": generate_password_hash("ghrtysT34a", method='sha256'),
            "userid": "mmartin"
        })
        self.collection_devices.insert_one({
            "srno": "R2018000012346A",
            "address": "4-6, Nakamachi, Setagaya, Tokyo, Japan",
            "uniqueid": "7712345678902",
            "macaddress": "",
            "ipaddress": "",
            "status": "P",
            "authcode": generate_password_hash("acbfgrR567",method='sha256'),
            "userid": "bmohanty"
        })
        self.collection_devices.insert_one({
            "srno": "R2018000012347A",
            "address": "4-7, Hannan Road, Taichung City, Taiwan",
            "uniqueid":"7712345678903",
            "macaddress": "",
            "ipaddress": "",
            "status":"P",
            "authcode": generate_password_hash("Gshsry231d",method='sha256'),
            "userid": "gdooley"
        })
        self.collection_devices.insert_one({
            "srno": "R2018000012348A",
            "address": "4-8, Pachukra Street, Paris, France",
            "uniqueid": "7712345678904",
            "macaddress": "",
            "ipaddress": "",
            "status": "P",
            "authcode": generate_password_hash("basdgJ834v",method='sha256'),
            "userid": "apachkura"
        })

if __name__ == '__main__':
    dummydata = MongoDBMgmt()
    dummydata.collection_devices.drop()
    dummydata.insert_devices()

