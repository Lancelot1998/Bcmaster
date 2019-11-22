# -*- coding: utf-8 -*-
"""
    Trans_sender
    ~~~~~~~~

    API for EOS

    :author: Jason Liu
"""

from flask import Flask, request, jsonify
import requests
import json
import subprocess 
import os
import random
import time

message = {
    "signatures": [],
    "compression": "none",
    "packed_context_free_data": "",
    "packed_trx": ""
}


def main():
    a = time.time()
    file = open("./message.txt")
    for line in file.readlines():
        line=line.strip('\n')
        signatures = list()
        signatures.append(line[0:101])
        message["signatures"] = signatures
        message["packed_trx"] = line[107:]
        print(message)
        r = requests.post('http://localhost:18888/v1/chain/push_transaction', data=json.dumps(message))
        #print(r.text)
        print("send one transaction")
    file.close()
    print("RPS = ", 10000 / (time.time() - a))

if __name__ == '__main__':
    main()
