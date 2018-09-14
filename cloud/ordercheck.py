#!flask/bin/python
from flask import Flask
from flask_pymongo import PyMongo, pymongo
import datetime
import time

app = Flask(__name__)
mongosecurity = PyMongo(app,uri="mongodb://localhost:27017/SecurityDB")
mongodatacollector = PyMongo(app,uri="mongodb://localhost:27017/CollectorDB")


def order_check():
    buy_orders = mongosecurity.db.Orders.find({'type': 'B', 'status': 'O'})
    sale_orders = mongosecurity.db.Orders.find({'type': 'S', 'status': 'O'})
    curtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S") #20180827115423
    contractid = "SC" + curtime
    if buy_orders and sale_orders:
        for buy_order in buy_orders:
            for sale_order in sale_orders:
                buyordqty = float(buy_order['qty'])
                buyrate = float(buy_order['unitrate'])
                saleordqty = float(sale_order['qty'])
                salerate = float(sale_order['unitrate'])
                if (buyordqty == saleordqty) and (buyrate >= salerate):
                    # Process Smart Contract
                    print("Processing Smart Contract - Execution")
                    insconfig = mongosecurity.db.SmartContract.insert_one(
                        {'contractid': contractid,'timestamp': curtime,
                         'uniqueid_buyer': buy_order['uniqueid'],'uniqueid_seller': sale_order['uniqueid'],
                         'contract_qty': buy_order['qty'],'contract_rate': buy_order['unitrate'],
                         'status': 'E',  # E-> Executed , F -> Fulfilled , S -> Settled
                         'fulfilltime':'','setltime':''})
                    seller_cur = mongosecurity.db.SwitchState.find({'uniqueid': sale_order['uniqueid']}).sort('timestamp', pymongo.DESCENDING).limit(1)
                    for seller_sw in seller_cur:
                        ins_switchstatelog = mongosecurity.db.StateLog.insert_one(
                            {'uniqueid': seller_sw['uniqueid'], 'timestamp': curtime,
                             'pv_supply': seller_sw['pv_supply'],
                             'bat_supply': seller_sw['bat_supply'],
                             'bat_charge': seller_sw['bat_charge'],
                             'ev_charge': seller_sw['ev_charge'],
                             'appl_supply': seller_sw['appl_supply'],
                             'grid_supply': 'OFF',  # seller_sw['grid_supply'],
                             'grid_dump': 'ON'})
                        print(seller_sw)
                        upd_sale_order = mongosecurity.db.Orders.update_one({'orderid': sale_order['orderid']}, {
                            '$set': {'status': 'C', 'contractid': contractid}})

                    buyer_cur = mongosecurity.db.SwitchState.find({'uniqueid': buy_order['uniqueid']}).sort('timestamp', pymongo.DESCENDING).limit(1)
                    for buyer_sw in buyer_cur:
                        ins_switchstatelog = mongosecurity.db.StateLog.insert_one(
                            {'uniqueid': buyer_sw['uniqueid'], 'timestamp': curtime,
                             'pv_supply': buyer_sw['pv_supply'],
                             'bat_supply': buyer_sw['bat_supply'],
                             'bat_charge': buyer_sw['bat_charge'],
                             'ev_charge': buyer_sw['ev_charge'],
                             'appl_supply': buyer_sw['appl_supply'],
                             'grid_supply': 'ON',  # buyer_sw['grid_supply'],
                             'grid_dump': 'OFF'})
                        print(buyer_sw)
                        upd_buy_order = mongosecurity.db.Orders.update_one({'orderid': buy_order['orderid']}, {
                            '$set': {'status': 'C', 'contractid': contractid}})
                    return True
    else:
        print("No Pending Orders to be fulfilled")
        return True

def contract_check():

    contractrecords = mongosecurity.db.SmartContract.find({'status': 'E'})
    if contractrecords:
        #Check the time duration and close the contract...
        curtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        for contract in contractrecords:
            contract_time = contract['timestamp']
            duration = float(curtime) - float(contract_time)
            if duration >= 300: #Process Contract closure after five minutes (for demo)...
                print("Processing Smart Contract - Fulfillment & Closure")
                seller_cur = mongosecurity.db.SwitchState.find({'uniqueid': contract['uniqueid_seller']}).sort('timestamp', pymongo.DESCENDING).limit(1)
                for seller_sw in seller_cur:
                    ins_switchstatelog = mongosecurity.db.StateLog.insert_one(
                        {'uniqueid': seller_sw['uniqueid'], 'timestamp': curtime,
                         'pv_supply': seller_sw['pv_supply'],
                         'bat_supply': seller_sw['bat_supply'],
                         'bat_charge': seller_sw['bat_charge'],
                         'ev_charge': seller_sw['ev_charge'],
                         'appl_supply': seller_sw['appl_supply'],
                         'grid_supply': 'OFF',  # seller_sw['grid_supply'],
                         'grid_dump': 'OFF'})
                    print(seller_sw)
                buyer_cur = mongosecurity.db.SwitchState.find({'uniqueid': contract['uniqueid_buyer']}).sort('timestamp', pymongo.DESCENDING).limit(1)
                for buyer_sw in buyer_cur:
                    ins_switchstatelog = mongosecurity.db.StateLog.insert_one(
                        {'uniqueid': buyer_sw['uniqueid'], 'timestamp': curtime,
                         'pv_supply': buyer_sw['pv_supply'],
                         'bat_supply': buyer_sw['bat_supply'],
                         'bat_charge': buyer_sw['bat_charge'],
                         'ev_charge': buyer_sw['ev_charge'],
                         'appl_supply': buyer_sw['appl_supply'],
                         'grid_supply': 'OFF',  # buyer_sw['grid_supply'],
                         'grid_dump': 'OFF'})
                    print(buyer_sw)
                upd_contract = mongosecurity.db.SmartContract.update_one({'contractid': contract['contractid']}, {
                    '$set': {'status': 'F', 'fulfilledtime': curtime}})
        return True
    else:
        print("All contracts are fulfilled. Nothing to process now.")
        return True

if __name__ == '__main__':
    while True:
        order_check()
        time.sleep(30)
        contract_check()
        time.sleep(30)
