import ecoboxlib as lib
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/status', methods=['GET'])
def devicestatus():
    p2ptrade = lib.get_switchstate('STATUS','p2ptrade')
    if p2ptrade == "ON":
        status = 'T' #Trade is going on...
    else:
        status = lib.get_switchstate('STATUS','status')
    curcfg = {'status': status,
              'hostname':lib.get_config('CONFIG','hostname'),
              'serialno':lib.get_config('CONFIG','serialno'),
              'uniqueid': lib.get_config('CONFIG', 'uniqueid'),
              'location':lib.get_config('CONFIG','location'),
              'address': lib.get_local_ip(lib.get_config('CONFIG','com_if')),
              'pv_supply':lib.get_switchstate('STATE','pv_supply'),
              'bat_supply':lib.get_switchstate('STATE','bat_supply'),
              'bat_charge':lib.get_switchstate('STATE','bat_charge'),
              'ev_charge':lib.get_switchstate('STATE','ev_charge'),
              'appl_supply': lib.get_switchstate('STATE','appl_supply'),
              'grid_supply': lib.get_switchstate('STATE', 'grid_supply'),
              'grid_dump': lib.get_switchstate('STATE', 'grid_dump')
              }
    return render_template('status.html', devicestatus = curcfg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9000)
