# -*- coding: utf-8 -*-
"""
    Trans_generator
    ~~~~~~~~

    API for Ethereum

    :author: Jason Liu
"""

from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

transaction = {
    "jsonrpc":"2.0",
    "method":"eth_sendTransaction",
    "params":[{
        "from": "0x491e431956c3e2326ac14606cafa265ba2742eea",
        "to": "0x06b0669105040838488d44b3ef9eb6710edb4134",
        "gas": "0xc000",
        "gasPrice": "0xa000",
        "value": "0x1",  
        "data": ""
    }],
    "id":1
}
headers = {'Content-Type': 'application/json'}

@app.route("/transaction", methods=['GET', 'POST'])
def transaction():
    r = requests.post('http://123.207.246.111:8545', data=json.dumps(transaction), headers=headers)
    print(r.text)


if __name__ == "__main__":
    app.run()

