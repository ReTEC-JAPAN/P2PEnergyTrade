#!/usr/bin/python
import netifaces as nif
import configparser
import requests as req

def get_local_ip(iface):  # 'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    if_ip = None
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)
        try:
            if i == iface:
                if_ip = addrs[nif.AF_INET][0]['addr']
        except IndexError and KeyError as KeyError:
            if_ip = None  ##ignore ifaces that doesn't have MAC or IP
    return if_ip

def get_local_macid(iface):  # 'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    if_mac = None
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)
        try:
            if i == iface:
                if_mac = addrs[nif.AF_LINK][0]['addr']
        except IndexError and KeyError as KeyError:
            if_mac = None  ##ignore ifaces that doesn't have MAC or IP
    return if_mac

def get_config(section, param):
    cfg = configparser.ConfigParser()
    cfg.read('initconf.ini')
    if cfg[section]:
        value = cfg[section][param]
        return value
    return ''

def get_switchstate(section,param):
    cfg = configparser.ConfigParser()
    cfg.read('switchstate.ini')
    if cfg[section]:
        return cfg[section][param]
    return ''

def modify_switchstate(section, param, value):
    cfg = configparser.ConfigParser()
    cfg.read('switchstate.ini')
    cfg.set(section, param, value)
    with open('switchstate.ini', 'w') as configfile:
        cfg.write(configfile)
    return True

def switch_relay(param,state):
    #Call hardware switching module.... to send the signal to the required port
    #read the HW port from initconf.ini file for switching config.
    #Modify switch state
    modify_switchstate('STATE',param,state)
    return True

def get_token():
    baseurl = get_config('CONFIG','cloudurl')
    srno = get_config('CONFIG','serialno')
    authcode = get_config('CONFIG','authcode')
    url = baseurl +"/discover/" + srno
    request = req.get(url, auth=(srno,authcode))
    resp=request.json()
    return(resp['token'])

def send_config():

    cfg = configparser.ConfigParser()
    cfg.read('initconf.ini')

    baseurl = cfg['CONFIG']['cloudurl']
    uniqueid = cfg['CONFIG']['uniqueid']
    macaddress = get_local_macid(cfg['CONFIG']['com_if'])
    ipaddress = cfg['CONFIG']['com_if']

    pv = cfg['INSTALLATION']['pv']
    pv_cap = cfg['INSTALLATION'][ 'pv_cap']
    pv_desc = cfg['INSTALLATION'][ 'pv_desc']

    bat = cfg['INSTALLATION'][ 'bat']
    bat_cap = cfg['INSTALLATION'][ 'bat_cap']
    bat_desc = cfg['INSTALLATION'][ 'bat_desc']

    ev = cfg['INSTALLATION']['ev']
    ev_cap = cfg['INSTALLATION']['ev_cap']
    ev_desc = cfg['INSTALLATION']['ev_desc']

    appl = cfg['INSTALLATION']['appl']
    appl_cap = cfg['INSTALLATION']['appl_cap']
    appl_desc = cfg['INSTALLATION']['appl_desc']

    token = get_switchstate('TOKEN','token')

    url = baseurl + "/discover/config/"+ uniqueid
    config_data = {'macaddress': macaddress, 'ipaddress': ipaddress,
                   'pv': pv, 'pv_cap': pv_cap, 'pv_desc': pv_desc,
                   'bat':bat,'bat_cap':bat_cap,'bat_desc':bat_desc,
                   'ev': ev, 'ev_cap': ev_cap,'ev_desc':ev_desc,
                   'appl': appl,'appl_cap': appl_cap,'appl_desc':appl_desc}
    header = {'x-access-token': format(token)}
    request = req.post(url, headers=header, json=config_data)
    resp = request.json()
    return resp

def send_meter_data():
    return True

def send_pinger():
    curstate = configparser.ConfigParser()
    curstate.read('switchstate.ini')

    pv_supply = curstate['STATE']['pv_supply']
    bat_supply = curstate['STATE']['bat_supply']
    bat_charge = curstate['STATE']['bat_charge']
    ev_charge = curstate['STATE']['ev_charge']
    appl_supply = curstate['STATE']['appl_supply']
    grid_supply = curstate['STATE']['grid_supply']
    grid_dump = curstate['STATE']['grid_dump']

    token = curstate['TOKEN']['token']

    baseurl = get_config('CONFIG','cloudurl')
    uniqueid = get_config('CONFIG','uniqueid')
    url = baseurl + "/pinger/" + uniqueid

    pinger_data = {'pv_supply': pv_supply, 'bat_supply': bat_supply,
                   'bat_charge': bat_charge, 'ev_charge': ev_charge, 'appl_supply': appl_supply,
                   'grid_supply': grid_supply, 'grid_dump': grid_dump}
    header = {'x-access-token': format(token)}
    request = req.post(url, headers=header, json=pinger_data)
    resp = request.json()
    print(resp)
    if 'status' in resp:
        modify_switchstate('STATUS','status',resp['status'])
        return True
    elif 'uniqueid' in resp:
        print(resp)
        print("Switch State Changed")
        modify_switchstate('STATE','pv_supply',resp['pv_supply'])
        modify_switchstate('STATE','bat_supply',resp['bat_supply'])
        modify_switchstate('STATE','bat_charge',resp['bat_charge'])
        modify_switchstate('STATE','ev_charge',resp['ev_charge'])
        modify_switchstate('STATE','appl_supply',resp['appl_supply'])
        modify_switchstate('STATE','grid_supply',resp['grid_supply'])
        modify_switchstate('STATE', 'grid_dump',resp['grid_dump'])
        if resp['grid_supply'] == 'ON' or resp['grid_dump'] == 'ON':
            modify_switchstate('STATUS','p2ptrade','ON')
        else:
            modify_switchstate('STATUS', 'p2ptrade', 'OFF')
        return True
    else:
        print(resp)
        return False