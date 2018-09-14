#!flask/bin/python
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class MongoDBMgmt:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['SecurityDB']
        self.collection_users = self.db['Users']
        self.collection_devices = self.db['EcoBoxes']
        self.collection_configs = self.db['Configs']
        self.collection_switchstate = self.db['SwitchState']
        self.collection_statelog = self.db['StateLog']
        self.collection_orders = self.db['Orders']
        self.collection_trends = self.db['Trends']

    def insert_trends(self):
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010000', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010100', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010200', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010300', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010400', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010500', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010600', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': -0.6, 'capacity_available': 6.5, 'buy_potential': 7.1, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010800', 'production': 1.5, 'consumption': 1.7,
             'grid_cons': -0.2, 'capacity_available': 6.5, 'buy_potential': 6.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707010900', 'production': 2.2, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 5.6, 'buy_potential': 5.6, 'sale_potential': 0.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011000', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 4, 'buy_potential': 4, 'sale_potential': 2.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011100', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 2, 'buy_potential': 2, 'sale_potential': 4.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011200', 'production': 3.4, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011300', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011400', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.1})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011500', 'production': 2.2, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 7.6})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011600', 'production': 1.5, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 0.6, 'buy_potential': 0.6, 'sale_potential': 5.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011800', 'production': 0, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 2.3, 'buy_potential': 2.3, 'sale_potential': 4.2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707011900', 'production': 0, 'consumption': 2.2,
             'grid_cons': 0, 'capacity_available': 4.5, 'buy_potential': 4.5, 'sale_potential': 2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707012000', 'production': 0, 'consumption': 2.3,
             'grid_cons': -0.3, 'capacity_available': 6.5, 'buy_potential': 6.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707012100', 'production': 0, 'consumption': 2.2,
             'grid_cons': -2.2, 'capacity_available': 6.5, 'buy_potential': 8.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707012200', 'production': 0, 'consumption': 1.7,
             'grid_cons': -1.7, 'capacity_available': 6.5, 'buy_potential': 8.2, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707012300', 'production': 0, 'consumption': 1.3,
             'grid_cons': -1.3, 'capacity_available': 6.5, 'buy_potential': 7.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020000', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020100', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020200', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020300', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020400', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020500', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020600', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': -0.6, 'capacity_available': 6.5, 'buy_potential': 7.1, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020800', 'production': 1.5, 'consumption': 1.7,
             'grid_cons': -0.2, 'capacity_available': 6.5, 'buy_potential': 6.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707020900', 'production': 2.2, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 5.6, 'buy_potential': 5.6, 'sale_potential': 0.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021000', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 4, 'buy_potential': 4, 'sale_potential': 2.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021100', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 2, 'buy_potential': 2, 'sale_potential': 4.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021200', 'production': 3.4, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021300', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021400', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.1})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021500', 'production': 2.2, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 7.6})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021600', 'production': 1.5, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 0.6, 'buy_potential': 0.6, 'sale_potential': 5.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021800', 'production': 0, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 2.3, 'buy_potential': 2.3, 'sale_potential': 4.2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707021900', 'production': 0, 'consumption': 2.2,
             'grid_cons': 0, 'capacity_available': 4.5, 'buy_potential': 4.5, 'sale_potential': 2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707022000', 'production': 0, 'consumption': 2.3,
             'grid_cons': -0.3, 'capacity_available': 6.5, 'buy_potential': 6.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707022100', 'production': 0, 'consumption': 2.2,
             'grid_cons': -2.2, 'capacity_available': 6.5, 'buy_potential': 8.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707022200', 'production': 0, 'consumption': 1.7,
             'grid_cons': -1.7, 'capacity_available': 6.5, 'buy_potential': 8.2, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707022300', 'production': 0, 'consumption': 1.3,
             'grid_cons': -1.3, 'capacity_available': 6.5, 'buy_potential': 7.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030000', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030100', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030200', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030300', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030400', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030500', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030600', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': -0.6, 'capacity_available': 6.5, 'buy_potential': 7.1, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030800', 'production': 1.5, 'consumption': 1.7,
             'grid_cons': -0.2, 'capacity_available': 6.5, 'buy_potential': 6.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707030900', 'production': 2.2, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 5.6, 'buy_potential': 5.6, 'sale_potential': 0.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031000', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 4, 'buy_potential': 4, 'sale_potential': 2.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031100', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 2, 'buy_potential': 2, 'sale_potential': 4.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031200', 'production': 3.4, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031300', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031400', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.1})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031500', 'production': 2.2, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 7.6})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031600', 'production': 1.5, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 0.6, 'buy_potential': 0.6, 'sale_potential': 5.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031800', 'production': 0, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 2.3, 'buy_potential': 2.3, 'sale_potential': 4.2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707031900', 'production': 0, 'consumption': 2.2,
             'grid_cons': 0, 'capacity_available': 4.5, 'buy_potential': 4.5, 'sale_potential': 2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707032000', 'production': 0, 'consumption': 2.3,
             'grid_cons': -0.3, 'capacity_available': 6.5, 'buy_potential': 6.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707032100', 'production': 0, 'consumption': 2.2,
             'grid_cons': -2.2, 'capacity_available': 6.5, 'buy_potential': 8.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707032200', 'production': 0, 'consumption': 1.7,
             'grid_cons': -1.7, 'capacity_available': 6.5, 'buy_potential': 8.2, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707032300', 'production': 0, 'consumption': 1.3,
             'grid_cons': -1.3, 'capacity_available': 6.5, 'buy_potential': 7.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040000', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040100', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040200', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040300', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040400', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040500', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040600', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': -0.6, 'capacity_available': 6.5, 'buy_potential': 7.1, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040800', 'production': 1.5, 'consumption': 1.7,
             'grid_cons': -0.2, 'capacity_available': 6.5, 'buy_potential': 6.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707040900', 'production': 2.2, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 5.6, 'buy_potential': 5.6, 'sale_potential': 0.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041000', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 4, 'buy_potential': 4, 'sale_potential': 2.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041100', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 2, 'buy_potential': 2, 'sale_potential': 4.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041200', 'production': 3.4, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041300', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041400', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.1})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041500', 'production': 2.2, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 7.6})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041600', 'production': 1.5, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 0.6, 'buy_potential': 0.6, 'sale_potential': 5.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041800', 'production': 0, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 2.3, 'buy_potential': 2.3, 'sale_potential': 4.2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707041900', 'production': 0, 'consumption': 2.2,
             'grid_cons': 0, 'capacity_available': 4.5, 'buy_potential': 4.5, 'sale_potential': 2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707042000', 'production': 0, 'consumption': 2.3,
             'grid_cons': -0.3, 'capacity_available': 6.5, 'buy_potential': 6.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707042100', 'production': 0, 'consumption': 2.2,
             'grid_cons': -2.2, 'capacity_available': 6.5, 'buy_potential': 8.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707042200', 'production': 0, 'consumption': 1.7,
             'grid_cons': -1.7, 'capacity_available': 6.5, 'buy_potential': 8.2, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707042300', 'production': 0, 'consumption': 1.3,
             'grid_cons': -1.3, 'capacity_available': 6.5, 'buy_potential': 7.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050000', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050100', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050200', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050300', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050400', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050500', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050600', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': -0.6, 'capacity_available': 6.5, 'buy_potential': 7.1, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050800', 'production': 1.5, 'consumption': 1.7,
             'grid_cons': -0.2, 'capacity_available': 6.5, 'buy_potential': 6.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707050900', 'production': 2.2, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 5.6, 'buy_potential': 5.6, 'sale_potential': 0.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051000', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 4, 'buy_potential': 4, 'sale_potential': 2.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051100', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 2, 'buy_potential': 2, 'sale_potential': 4.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051200', 'production': 3.4, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051300', 'production': 3.1, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051400', 'production': 2.7, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 8.1})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051500', 'production': 2.2, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 7.6})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051600', 'production': 1.5, 'consumption': 1.1,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051700', 'production': 0.7, 'consumption': 1.3,
             'grid_cons': 0, 'capacity_available': 0.6, 'buy_potential': 0.6, 'sale_potential': 5.9})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051800', 'production': 0, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 2.3, 'buy_potential': 2.3, 'sale_potential': 4.2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707051900', 'production': 0, 'consumption': 2.2,
             'grid_cons': 0, 'capacity_available': 4.5, 'buy_potential': 4.5, 'sale_potential': 2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707052000', 'production': 0, 'consumption': 2.3,
             'grid_cons': -0.3, 'capacity_available': 6.5, 'buy_potential': 6.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707052100', 'production': 0, 'consumption': 2.2,
             'grid_cons': -2.2, 'capacity_available': 6.5, 'buy_potential': 8.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707052200', 'production': 0, 'consumption': 1.7,
             'grid_cons': -1.7, 'capacity_available': 6.5, 'buy_potential': 8.2, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707052300', 'production': 0, 'consumption': 1.3,
             'grid_cons': -1.3, 'capacity_available': 6.5, 'buy_potential': 7.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060000', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060100', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060200', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060300', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060400', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060500', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060600', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060700', 'production': 0.7, 'consumption': 0.8,
             'grid_cons': -0.1, 'capacity_available': 6.5, 'buy_potential': 6.6, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060800', 'production': 1.5, 'consumption': 1.2,
             'grid_cons': 0, 'capacity_available': 6.2, 'buy_potential': 6.2, 'sale_potential': 0.3})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707060900', 'production': 2.2, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 5.7, 'buy_potential': 5.7, 'sale_potential': 0.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061000', 'production': 2.7, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 4.7, 'buy_potential': 4.7, 'sale_potential': 1.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061100', 'production': 3.1, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 3.3, 'buy_potential': 3.3, 'sale_potential': 3.2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061200', 'production': 3.4, 'consumption': 2,
             'grid_cons': 0, 'capacity_available': 1.9, 'buy_potential': 1.9, 'sale_potential': 4.6})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061300', 'production': 3.1, 'consumption': 2,
             'grid_cons': 0, 'capacity_available': 0.79, 'buy_potential': 0.79,
             'sale_potential': 5.7})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061400', 'production': 2.7, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.7})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061500', 'production': 2.2, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 7})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061600', 'production': 1.5, 'consumption': 1.5,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061700', 'production': 0.7, 'consumption': 1.5,
             'grid_cons': 0, 'capacity_available': 0.8, 'buy_potential': 0.8, 'sale_potential': 5.7})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061800', 'production': 0, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 2.5, 'buy_potential': 2.5, 'sale_potential': 4})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707061900', 'production': 0, 'consumption': 2.2,
             'grid_cons': 0, 'capacity_available': 4.7, 'buy_potential': 4.7, 'sale_potential': 1.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707062000', 'production': 0, 'consumption': 2.3,
             'grid_cons': -0.5, 'capacity_available': 6.5, 'buy_potential': 7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707062100', 'production': 0, 'consumption': 2.2,
             'grid_cons': -2.2, 'capacity_available': 6.5, 'buy_potential': 8.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707062200', 'production': 0, 'consumption': 1.7,
             'grid_cons': -1.7, 'capacity_available': 6.5, 'buy_potential': 8.2, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707062300', 'production': 0, 'consumption': 1.3,
             'grid_cons': -1.3, 'capacity_available': 6.5, 'buy_potential': 7.8, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070000', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070100', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070200', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070300', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070400', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070500', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070600', 'production': 0, 'consumption': 0.8,
             'grid_cons': -0.8, 'capacity_available': 6.5, 'buy_potential': 7.3, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070700', 'production': 0.7, 'consumption': 0.8,
             'grid_cons': -0.1, 'capacity_available': 6.5, 'buy_potential': 6.6, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070800', 'production': 1.5, 'consumption': 1.2,
             'grid_cons': 0, 'capacity_available': 6.2, 'buy_potential': 6.2, 'sale_potential': 0.3})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707070900', 'production': 2.2, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 5.7, 'buy_potential': 5.7, 'sale_potential': 0.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071000', 'production': 2.7, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 4.7, 'buy_potential': 4.7, 'sale_potential': 1.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071100', 'production': 3.1, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 3.3, 'buy_potential': 3.3, 'sale_potential': 3.2})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071200', 'production': 3.4, 'consumption': 2,
             'grid_cons': 0, 'capacity_available': 1.9, 'buy_potential': 1.9, 'sale_potential': 4.6})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071300', 'production': 3.1, 'consumption': 2,
             'grid_cons': 0, 'capacity_available': 0.8, 'buy_potential': 0.8,
             'sale_potential': 5.7})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071400', 'production': 2.7, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.7})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071500', 'production': 2.2, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 7})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071600', 'production': 1.5, 'consumption': 1.5,
             'grid_cons': 0, 'capacity_available': 0, 'buy_potential': 0, 'sale_potential': 6.5})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071700', 'production': 0.7, 'consumption': 1.5,
             'grid_cons': 0, 'capacity_available': 0.8, 'buy_potential': 0.8, 'sale_potential': 5.7})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071800', 'production': 0, 'consumption': 1.7,
             'grid_cons': 0, 'capacity_available': 2.5, 'buy_potential': 2.5, 'sale_potential': 4})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707071900', 'production': 0, 'consumption': 2.2,
             'grid_cons': 0, 'capacity_available': 4.7, 'buy_potential': 4.7, 'sale_potential': 1.8})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707072000', 'production': 0, 'consumption': 2.3,
             'grid_cons': -0.5, 'capacity_available': 6.5, 'buy_potential': 7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707072100', 'production': 0, 'consumption': 2.2,
             'grid_cons': -2.2, 'capacity_available': 6.5, 'buy_potential': 8.7, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707072200', 'production': 0, 'consumption': 1.7,
             'grid_cons': -1.7, 'capacity_available': 6.5, 'buy_potential': 8.2, 'sale_potential': 0})
        self.collection_trends.insert_one(
            {'uniqueid': '7712345678903', 'timestamp': '201707072300', 'production': 0, 'consumption': 1.3,
             'grid_cons': -1.3, 'capacity_available': 6.5, 'buy_potential': 7.8, 'sale_potential': 0})


if __name__ == '__main__':
    dummydata = MongoDBMgmt()
    dummydata.collection_trends.drop()
    dummydata.insert_trends()

