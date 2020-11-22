#!/bin/bash
sudo docker exec -it peer0.org2.example.com bash -c "peer chaincode query -C mychannel -n qscc -c '{\"Args\":[\"GetBlockByTxID\", \"mychannel\",\"$1\"]}'"

