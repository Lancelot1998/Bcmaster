# -*- coding: utf-8 -*-
"""
    Trans_generator
    ~~~~~~~~

    API for Parity

    :author: Jason Liu
"""

from flask import Flask, request, jsonify
import requests
import json
import time

app = Flask(__name__)


transaction = {"method": "eth_sendTransaction", 
    "params": [{
    "from": "0x4812d83af41ab9561f29d759c4d17988b450618e",
    "to": "0xbf7b84b05f7d9fd475c1e9e21979f7321eee26e9",
    "gas": "0x76c0", 
    "gasPrice": "0x9184e72a000", 
    "value": "0x00001", 
    "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }],
    "id": 1,
    "jsonrpc": "2.0"
}
headers = {'Content-Type': 'application/json'}

account = {"method": "personal_unlockAccount",
    "params":["0x4812d83af41ab9561f29d759c4d17988b450618e", "123", None],
    "id": 1, 
    "jsonrpc": "2.0"
}
times = time.time()
for i in range(1, 1000):
    r = requests.post('http://localhost:8545', data=json.dumps(account), headers=headers)
    r = requests.post('http://localhost:8545', data=json.dumps(transaction), headers=headers)
    print(r.text)

print("RPS = ", 1000/(time.time() - times))
