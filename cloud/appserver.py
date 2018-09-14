#!flask/bin/python
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_pymongo import PyMongo, pymongo
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


app = Flask(__name__)

mongosecurity = PyMongo(app,uri="mongodb://localhost:27017/SecurityDB")
mongodatacollector = PyMongo(app,uri="mongodb://localhost:27017/CollectorDB")
# mongotrade = PyMongo(app,uri="mongodb://localhost:27017/P2PTradingDB")

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
            input_userid = request.form['userid']
            dbuser = mongosecurity.db.Users.find_one({'userid': input_userid})
            if dbuser: # User found
                if check_password_hash(dbuser['passwd'],request.form['passwd']):
                    session['username'] = request.form['userid']
                    return redirect(url_for('dashboard'))
            return  redirect(url_for('register')) #'Invalid username/password combination'
    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout')
@is_logged_in
def logout():
     if session['username']:
         session.clear()
     return redirect(url_for('login'))

@app.route('/dashboard')
@is_logged_in
def dashboard():
    userid = session['username']
    regdevice = mongosecurity.db.EcoBoxes.find_one({'userid': userid})
    if regdevice:
        uniqueid = regdevice['uniqueid']
        configs = mongosecurity.db.Configs.find_one({'uniqueid': uniqueid})
        swstate_cur = mongosecurity.db.SwitchState.find({'uniqueid': uniqueid}).sort('timestamp',pymongo.DESCENDING).limit(1)
        swstate = {}
        for switchstate in swstate_cur:
            swstate = switchstate
        orders = mongosecurity.db.Orders.find({'uniqueid': uniqueid})
        contracts = mongosecurity.db.SmartContract.find({'$or':[{'uniqueid_buyer':uniqueid},{'uniqueid_seller': uniqueid}]})
        #for contract in contracts:
        #    print(contract)
        return render_template('dashboard.html', device = regdevice, configs = configs, switches = swstate, orderlist = orders, contracts = contracts )
    else:
        return redirect(url_for('register'))

@app.route('/trends', methods=['GET'])
@is_logged_in
def trends():
    userid = session['username']
    regdevice = mongosecurity.db.EcoBoxes.find_one({'userid': userid})
    if regdevice:
        print("Unique ID:" + regdevice['uniqueid'])
        trenddata = mongosecurity.db.Trends.find({'uniqueid': regdevice['uniqueid']})
        print("Trend Data Reported:")
        print(trenddata)
        return render_template('trends.html', trends = trenddata)
    else:
        return redirect(url_for('register'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # Do all form validation
        if request.form['devicesrno']:
            # Find EcoBox Authentication Code and Match with supplied code here...
            device_selected = mongosecurity.db.EcoBoxes.find_one({'srno': request.form['devicesrno'],'status':'I'})
            if device_selected:
                dbauthcode = device_selected['authcode']
                if check_password_hash(dbauthcode, request.form['authcode']):
                    dbuser = mongosecurity.db.Users.insert_one({
                            "userid": request.form['userid'],
                            "name": request.form['name'],
                            "passwd": generate_password_hash(request.form['passwd'],method='sha256'),
                            "email": request.form['email'],
                            "billing-address": request.form['billing-address'],
                            "keypair": request.form['keypair']})
                    upddevice = mongosecurity.db.EcoBoxes.update_one({'srno': request.form['devicesrno']}, {'$set':{'userid':request.form['userid'],'status': 'R'}},upsert=False)
                    session['username'] = request.form['userid']
                    return redirect(url_for('dashboard'))
                else:
                    return "Invalid Serial No and Authorization Code combination"
            else:
                return "Device not found"
    else:
        devicelist = mongosecurity.db.EcoBoxes.find()
        return render_template('registerbox.html',devicelist = devicelist )

# Fetch all un-associated boxes from database and display
@app.route('/boxes')
def boxes():
    #devicelist = mongosecurity.db.EcoBoxes.find({'status':'I'})
    devicelist = mongosecurity.db.EcoBoxes.find()
    return render_template('boxlist.html',devicelist = devicelist)

@app.route('/orders', methods=['GET','POST'])
@is_logged_in
def place_order():
    userid = session['username']
    if request.method == 'POST':
        regdevice = mongosecurity.db.EcoBoxes.find_one({'userid': userid})
        if regdevice:
            #register orders ...
            curtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            orderid = "ORD" + curtime
            dborder = mongosecurity.db.Orders.insert_one({'orderid': orderid, 'userid': userid,
                                                      'uniqueid': regdevice['uniqueid'],
                                                      'timestamp': curtime,
                                                      'type': request.form['ordertype'],
                                                      'qty': request.form['qty'],
                                                      'unitrate': request.form['rate'],
                                                      'status':'O',       # Order is OPEN, C -> Contracted, F -> Fulfilled
                                                      'contractid':''})
            return redirect(url_for('dashboard'))
    else:
        return render_template('orders.html')

@app.route('/admin')
@is_logged_in
def admin():
    ecoboxes = mongosecurity.db.EcoBoxes.find()
    configs = mongosecurity.db.Configs.find()
    users = mongosecurity.db.Users.find()
    orders = mongosecurity.db.Orders.find()
    switchstates = mongosecurity.db.SwitchState.find() #.sort({"timestamp": -1}).limit(10)
    statelogs = mongosecurity.db.StateLog.find()
    return render_template('admin.html', devicelist = ecoboxes, configlist = configs, userlist = users, orderlist = orders, switchlist = switchstates, statelogs = statelogs )

if __name__ == '__main__':
    app.secret_key = 'retcweb'
    app.run(debug=True, host='0.0.0.0', port=8000)
