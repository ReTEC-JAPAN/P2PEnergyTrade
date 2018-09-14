source ~/cloud-retc/venv/bin/activate
nohup mongod --dbpath /home/ubuntu/cloud-retc/db > ~/cloud-retc/log/mongodb.log &
nohup python3 ~/cloud-retc/appserver.py > ~/cloud-retc/log/appserver.log &
nohup python3 ~/cloud-retc/datacollector.py > ~/cloud-retc/log/datacollector.log &
nohup python3 ~/cloud-retc/ordercheck.py > ~/cloud-retc/log/ordercheck.log &
deactivate