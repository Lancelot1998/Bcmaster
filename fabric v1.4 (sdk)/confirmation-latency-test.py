# -*- coding: utf-8 -*-
"""
    Trans_generator
    ~~~~~~~~

    API for Fabric v1.4

    :author: Jason Liu
"""

import requests
import json
import os
import time
import random
import subprocess
from prometheus_client import start_http_server,Gauge,Histogram

ard_histogram=Histogram("Tx_Duration","buckets of duration",buckets=[0,0.05,0.10,0.15,0.20,0.3,0.4,0.5,0.6,0.7])
ard_gauge=Gauge("Tx_ARD","instant of duration")

start_http_server(13456)
result = {
  "peers": ["peer0.org1.example.com","peer0.org2.example.com"],
  "fcn":"move",
  "args":["a","b","1"]
}
headers = {"content-type": "application/json",
           "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODUzMTg0MzEsInVzZXJuYW1lIjoiSmFzIiwib3JnTmFtZSI6Ik9yZzIiLCJpYXQiOjE1ODUyODI0MzF9.NmNpF2nb77hpQzL3FDZG5mB1KGfcS0lkosfsjgJkg9A"}

#r = requests.post('http://localhost:4000/channels/mychannel/chaincodes/mycc', data=json.dumps(result), headers=headers)
#print(r.text)
#hash_ = r.text[-66:-2]
#print(hash_)
#arg0 = hash_
#os.system("sudo ./docker.sh")
arg_2 = 70000
for i in range(100000):
    # times = time.time()
    result = os.popen('./docker.sh ' + str(arg_2))  
    # times = time.time()
    result_ = result.read()
    # for line in result_.splitlines():  
    #    print(line)
    arg_2 += 1
    times = time.time()
    # print(time.time() - times)
    print("result is", result_.splitlines()[1][-126:-62])
    hash_ = result_.splitlines()[1][-126:-62]

    while(True):
        time_1 = time.time()
        sub = subprocess.Popen('./docker2.sh ' + str(hash_), shell=True, stdout=subprocess.PIPE)
        print(time.time() - time_1)
        # sub = subprocess.Popen('./docker2.sh ' + "0x4910470174017491004179012", shell=True, stdout=subprocess.PIPE)
        content = str(sub.stdout.read())
        # print(time.time() - time_1)
        if "txID" in content:
            print("false")
            pass
        else:
            latency = time.time() - times
            print(latency)
            ard_histogram.observe(latency)
            ard_gauge.set(latency)
            break
    time.sleep(20)
    



