# -*- coding: utf-8 -*-
"""
    Fabric v1.4 API Server (Using Fabric Python SDK)
    ~~~~~~~~

    Automatic Transaction Generator

    :author: Jason Liu
"""
from hfc.fabric import Client
import asyncio
import time

loop = asyncio.get_event_loop()
cli = Client(net_profile="./network.json")

print(cli.organizations)  # orgs in the network
print(cli.peers)  # peers in the network
print(cli.orderers)  # orderers in the network
print(cli.CAs)  # ca nodes in the network
cli.new_channel('mychannel')
org1_admin = cli.get_user(org_name='org1.example.com', name='Admin') # get the admin user from local path
args = ["212344", "red", "202", "Jack"]
#args2 = ["GetBlockByTxID", "mychannel", "64caff9786483d0d56f6d7ba738ece33328c2559b7b4093547018bcd22e42986"]
# The response should be true if succeed
response = loop.run_until_complete(cli.query_instantiated_chaincodes(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com'],
               decode=True
               ))
"""
# This part is used to check the channel information
response = loop.run_until_complete(cli.query_peers(
               requestor=org1_admin,
               peer='peer0.org1.example.com',
               channel='mychannel',
               local=True,
               decode=True
               ))
print("response=", response)
"""

for i in range(400000000, 5000000000):
    time_1 = time.time()
    args = [str(i), "red", "202", "Jack"]
    response = loop.run_until_complete(cli.chaincode_invoke(
                   requestor=org1_admin,
                   channel_name='mychannel',
                   peers=['peer0.org1.example.com', 'peer0.org2.example.com'],
                   args=args,
                   cc_name='marbles',
                   fcn='initMarble',
                   transient_map=None, # optional, for private data
                   wait_for_event=False, # for being sure chaincode invocation has been commited in the ledger, default is on tx event
                   #cc_pattern='^invoked*' # if you want to wait for chaincode event and you have a `stub.SetEvent("invoked", value)` in your chaincode
                   ))
    time_2 = time.time() - time_1
    print("throughput= ", 1/time_2)

#print("response=", response)
