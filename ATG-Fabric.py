# -*- coding: utf-8 -*-
"""
    Trans_generator
    ~~~~~~~~

    API for Fabric v0.6

    :author: Jason Liu
"""

from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)
result = {
  "jsonrpc": "2.0",
  "method": "invoke",
  "params": {
      "type": 1,
      "chaincodeID":{
          "name":"a94e976cc0a8c78bb8e9d881c7c700dc358b8ae58b7e08ddd69e263d39b07d5f369b9fe46ce88dcf77b0f7ad9aec3bd997ab0e8fb4070b82f7ad7d996b13e497"
      },
      "ctorMsg": {
         "function":"invoke",
         "args":["a", "b", "1"]
      }
  },
  "id": 3
}


@app.route("/transaction", methods=['GET', 'POST'])
def transaction():
    r = requests.post('http://localhost:7050/chaincode', data=json.dumps(result))
    print(r.text)


if __name__ == "__main__":
    app.run()
