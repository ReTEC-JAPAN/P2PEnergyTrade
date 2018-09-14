#!/bin/bash

nohup python3 /retc/EcoBox/ecoboxstatus.py > /retc/EcoBox/log/status.log &
nohup python3 /retc/EcoBox/initialize.py > /retc/EcoBox/log/initialize.log &

while true
do
    nohup sudo python3 /retc/EcoBox/led_status_display.py >> /retc/EcoBox/log/ledstatus.log &
    sleep 20
done