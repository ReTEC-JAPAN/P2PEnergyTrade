#!flask/bin/python
from flask import Flask, request, jsonify, make_response
from flask_pymongo import PyMongo
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import time

app = Flask(__name__)

mongosecurity = PyMongo(app,uri="mongodb://localhost:27017/SecurityDB")
mongodatacollector = PyMongo(app,uri="mongodb://localhost:27017/CollectorDB")

def auth_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        auth = request.authorization
        if auth:
            # Use the serial number as username and authkey as password
            device_connected = mongosecurity.db.EcoBoxes.find_one({'srno': auth.username})
            if device_connected: #Found the provisioned device
                if check_password_hash(device_connected["authcode"],auth.password):
                    return f(*args, **kwargs)
                else:
                    #return jsonify({'Auth Code DB': device_connected["authcode"], 'Auth Code Supplied': auth.password})
                    return jsonify({'message' : 'Authorization Code is not valid'})
            else:
                #return jsonify({'Auth Code DB': device_connected["authcode"], 'Auth Code Supplied': auth.password})
                return jsonify({'message' :'Device Serial Number is not valid'})
        else:
            return jsonify({'message' : 'Authorization Required'})
    return wrap

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            device = mongosecurity.db.EcoBoxes.find_one({'srno': data['srno']})
            serialno = device['srno']
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401
        return f(serialno,*args, **kwargs) #f(device['srno'], *args, **kwargs)
    return decorated

@app.route('/discover/<string:boxsrno>', methods=['GET'])
@auth_required
def discover(boxsrno):
    if request.method == 'GET':
        auth = request.authorization
        device_connected = mongosecurity.db.EcoBoxes.find_one({'srno': boxsrno})
        if device_connected:
            # Find EcoBox Authentication Code and Match with supplied code here...
            dbauthcode = device_connected["authcode"]
            authcode = auth.password
            if device_connected["status"]== 'P':
                if check_password_hash(dbauthcode,authcode):
                    upddevice = mongosecurity.db.EcoBoxes.update_one({'srno': boxsrno}, {'$set':{'status': 'I'},},upsert=False)
            token = jwt.encode({'srno': boxsrno,
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=720)},
                                app.config['SECRET_KEY'])
            return jsonify({'token': token.decode('UTF-8')})
        else:
            return jsonify({'message' : 'Device not found'})
    return jsonify({'message' : 'No Get Request'})

@app.route('/discover/config/<string:uniqueid>', methods=['POST'])
@token_required
def update_config(serialno, uniqueid):
    if request.method == 'POST':
        config_data = request.get_json()
        macaddress = config_data['macaddress']
        ipaddress = config_data['ipaddress']
        pv_exist = config_data['pv']
        pv_cap = config_data['pv_cap']
        pv_desc = config_data['pv_desc']
        bat_exist = config_data['bat']
        bat_cap = config_data['bat_cap']
        bat_desc = config_data['bat_desc']
        ev_exist = config_data['ev']
        ev_cap = config_data['ev_cap']
        ev_desc = config_data['ev_desc']
        appl = config_data['appl']
        appl_cap = config_data['appl_cap']
        appl_desc = config_data['appl_desc']
        curtime = datetime.datetime.now().strftime("%Y%m%d%H%M")
        upddevice = mongosecurity.db.EcoBoxes.update_one({'srno': serialno},
                                                         {'$set':{'macaddress':macaddress,'ipaddress': ipaddress,
                                                                  'uniqueid': uniqueid, 'status': 'I'},},upsert=False)
        insconfig = mongosecurity.db.Configs.insert_one({'uniqueid': uniqueid, 'timestamp': curtime, 'synchstatus': 'S',
                                                         'pv' : pv_exist, 'pv_cap':pv_cap,'pv_desc': pv_desc,
                                                        'bat': bat_exist,'bat_cap': bat_cap,'bms_desc': bat_desc,
                                                        'ev': ev_exist,'ev_cap': ev_cap,'ev_desc': ev_desc,
                                                        'appl': appl, 'appl_cap': appl_cap,'appl_desc': appl_desc})
        return jsonify({'message' : 'SUCCESS'})
    return jsonify({'message' : 'FAILED'})

@app.route('/pinger/<string:uniqueid>', methods=['POST'])
@token_required
def state_check(serialno,uniqueid):
    if request.method == 'POST':
        config_data = request.get_json()
        #print(config_data)
        pv_supply = config_data['pv_supply']
        bat_supply = config_data['bat_supply']
        bat_charge = config_data['bat_charge']
        ev_charge = config_data['ev_charge']
        appl_supply = config_data['appl_supply']
        grid_supply = config_data['grid_supply']
        grid_dump = config_data['grid_dump']
        curtime = datetime.datetime.now().strftime("%Y%m%d%H%M")

        insconfig = mongosecurity.db.SwitchState.insert_one({'uniqueid': uniqueid, 'timestamp': curtime, 'pv_supply' : pv_supply, 'bat_supply':bat_supply,
                                                             'bat_charge': bat_charge,'ev_charge': ev_charge,'appl_supply': appl_supply,
                                                             'grid_supply': grid_supply,'grid_dump': grid_dump})

        device = mongosecurity.db.EcoBoxes.find_one({'srno': serialno})
        status = device['status']
        newstate = mongosecurity.db.StateLog.find_one({'uniqueid': uniqueid})
        if newstate:
                switchstate = {'uniqueid': newstate['uniqueid'], 'timestamp': curtime,
                               'pv_supply' : newstate['pv_supply'], 'bat_supply': newstate['bat_supply'],
                                'bat_charge': newstate['bat_charge'],'ev_charge': newstate['ev_charge'],'appl_supply': newstate['appl_supply'],
                                'grid_supply': newstate['grid_supply'],'grid_dump': newstate['grid_dump']}
                del_state_log_rec = mongosecurity.db.StateLog.delete_one({'uniqueid': uniqueid})
                return jsonify(switchstate)
        else:
            return jsonify({'status': status})
    return jsonify({'message' : 'FAILED'})


if __name__ == '__main__':

    app.secret_key = 'retcapi'
    app.run(debug=True,host='0.0.0.0', port=8080)

