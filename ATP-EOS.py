# -*- coding: utf-8 -*-
"""
    Trans_packer
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

data = {
    "action": "transfer",
    "args": {
        "to": "eos",
        "memo": "4034",
        "from": "eosio",
        "quantity": "1.0000 EOS"
    },
    "code": "eosio.token"
}

transaction = {
    "expiration": "2019-07-11T7:00:36",
    "ref_block_num": 50606,
    "ref_block_prefix": 2198786751,
    "max_net_usage_words": 0,
    "max_cpu_usage_ms": 0,
    "delay_sec": 0,
    "context_free_actions": [],
    "actions": [{
        "account": "eosio.token",
        "name": "transfer",
        "authorization": [{
            "actor": "eosio",
            "permission": "active"
        }],
        "data": "0000000000ea30550000000000003055102700000000000004454f53000000000434303334"
    }],
    "transaction_extensions": []
}

block = {
    "block_num_or_id":1111
}

message = {
    "signatures": [],
    "compression": "none",
    "packed_context_free_data": "",
    "packed_trx": ""
}

priv_key = "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"
transpool_size = 100

def main():
    os.system('rm record.json')
    os.system('touch record.json')
    os.system('rm message.txt')
    os.system('touch message.txt')
    for i in range(0, transpool_size):
        memo = str(random.randint(2000, 4000))
        data["args"]["memo"] = memo
        r = requests.post('http://localhost:18888/v1/chain/abi_json_to_bin', data=json.dumps(data))
        current_data = json.loads(r.text)
        #print(current_data)
        transaction["actions"][0]["data"] = current_data["binargs"]
        r = requests.get('http://localhost:18888/v1/chain/get_info')
        current_block = json.loads(r.text)
        transaction["ref_block_num"] = current_block["head_block_num"]
        block["block_num_or_id"] = current_block["head_block_num"]
        #print(type(block["block_num_or_id"]))
        r = requests.post('http://localhost:18888/v1/chain/get_block', data=json.dumps(block))
        current_prefix = json.loads(r.text)
        transaction["ref_block_prefix"] = current_prefix["ref_block_prefix"]
        #transaction["ref_block_num"] = current_prefix["id"]
        #print(transaction)
        with open("./record.json","w") as f:
            json.dump(transaction, f)
        with os.popen('cleos -u http://localhost:18888 convert pack_transaction %s' % "./record.json") as p:
            result_tx = p.read()
        result_tx = json.loads(result_tx)
        #print(result_tx["packed_trx"])
        with os.popen('cleos -u http://localhost:18888 sign -k 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3 %s' % "./record.json") as p:
            result_sig = p.read()
        result_sig = json.loads(result_sig)
        #print("\n\n")
        #print(result_sig["signatures"][0])
        #print(type(result_sig["signatures"][0]))
        message["packed_trx"] = result_tx["packed_trx"]
        message["signatures"] = result_sig["signatures"]
        #message = json.dumps(message)
        #print(message)
        r = requests.post('http://localhost:18888/v1/chain/push_transaction', data=json.dumps(message))
        #print(r.text)
        print("pack one trans successfully")
        with open("./message.txt","a") as f:
            f.write(message["signatures"][0] + "PACKED" + message["packed_trx"] + "\n")


if __name__ == '__main__':
    main()
