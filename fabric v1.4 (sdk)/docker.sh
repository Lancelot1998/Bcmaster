#!/bin/bash
echo $1
ORDERER_CA=/etc/hyperledger/msp/orderer/msp/tlscacerts/tlsca.example.com-cert.pem
sudo docker exec -it peer0.org1.example.com bash -c "peer chaincode invoke -o orderer.example.com:7050 --tls true --cafile $ORDERER_CA --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /etc/hyperledger/msp/peer/tls/ca.crt --peerAddresses peer0.org2.example.com:7051 --tlsRootCertFiles /etc/hyperledger/msp/peer2/tls/ca.crt --waitForEvent -n marbles -c '{\"Args\":[\"initMarble\",\"$1\",\"red\",\"202\",\"Jack\"]}' -C mychannel"
# sudo docker exec -it peer1.org2.example.com bash -c "peer chaincode query -C mychannel -n qscc -c '{\"Args\":[\"GetBlockByTxID\", \"mychannel\",\"$1\"]}'"
# sudo docker exec -it peer0.org1.example.com bash -c "peer chaincode invoke -o orderer.example.com:7050 --tls true --cafile $ORDERER_CA --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /etc/hyperledger/msp/peer/tls/ca.crt --peerAddresses peer0.org2.example.com:7051 --tlsRootCertFiles /etc/hyperledger/msp/peer2/tls/ca.crt -n marbles -c '{\"Args\":[\"initMarble\",\"$1\",\"red\",\"202\",\"Jack\"]}' -C mychannel"

