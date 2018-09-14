from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import datetime



class MongoDBMgmt:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['SecurityDB']
        self.collection_users = self.db['Users']

    def insert_user(self):
        self.collection_users.insert_one({
            "userid": "bmohanty",
            "name": "Bikash K Mohanty",
            "passwd": "bmohanty",
            "email": "Bikash.Mohanty@retc.io",
            "billingaddr": "2-3-4 Hanamachi, Adachi-Ku, Tokyo, JAPAN",
            "keypair": ""
        })
        self.collection_users.insert_one({
            "userid": "mmesmer",
            "name": "Martin Mesmer",
            "passwd": "mmesmer",
            "email": "Martin.Mesmer@retc.io",
            "billingaddr": "1-2-3 Mita, Chiyoda-Ku, Tokyo, JAPAN",
            "keypair": ""
        })
        self.collection_users.insert_one({
            "userid": "apachurka",
            "name": "Amaury Pachurka ",
            "passwd": "apachurka",
            "email": "Amaury.Pachurka@retc.io",
            "billingaddr": "#23 Fashion Street, Section-2, Paris",
            "keypair": ""
        })
        self.collection_users.insert_one({
            "userid": "gdooley",
            "name": "Gareth Dooley",
            "passwd": "gdooley",
            "email": "Gareth.Dooley@retc.io",
            "billingaddr": "#675 Hanan Road, 3F, 488,Taichung City, Taiwan",
            "keypair": ""
        })


if __name__ == '__main__':
    dummydata = MongoDBMgmt()
    dummydata.collection_users.drop()
    dummydata.insert_user()
