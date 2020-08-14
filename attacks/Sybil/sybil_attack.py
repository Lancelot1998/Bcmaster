# coding=utf-8
"""
A simulated Sybil attack against blockchain.
"""
import random

honest_peer = list() # the list of honest peer
honest_peer.append('172.18.127.129')
honest_peer.append('172.18.127.128')
honest_peer.append('172.18.127.127')
honest_peer.append('172.18.127.126')
honest_peer.append('172.18.127.125')

sybil_peer = list()  # the IP address of Sybil attackers
sybil_peer.append('172.18.127.124')
sybil_peer.append('172.18.127.123')
sybil_peer.append('172.18.127.122')
sybil_peer.append('172.18.127.121')
sybil_peer.append('172.18.127.120')

peers = honest_peer + sybil_peer # all peers 
relationship = dict()

# initial peer distribution
peer_list = dict()
for peer in honest_peer:
    peer_list[peer] = list()
    for index in range(2):
    	peer_index = random.randint(0, len(peers) - 1)
    	if peers[peer_index] is not peer and peers[peer_index] not in peer_list[peer]:
            flag = 0
            for i in peer_list.values():
                if peers[peer_index] not in i:
                    pass
                else:
                    flag = 1
            if flag is 0:
                peer_list[peer].append(peers[peer_index])    		

# print(peer_list)

# adjustment
peer_num = dict()
for node in peers:
    peer_num[node] = 0
    for peer in peer_list.keys():
        if peer is node:
            peer_num[node] += len(peer_list[peer])
        else:
            pass
    temp = peer_list.values()
    for i in temp:
        for j in i:
            if j is node:
                peer_num[node] += 1

# print(peer_num)

for peer in honest_peer:
    if peer_num[peer] is 0:
        peer_index = random.randint(len(sybil_peer), len(peers) - 1)
        peer_list[peer].append(peers[peer_index])
        peer_num[peer] += 1
        peer_num[peers[peer_index]] += 1

# print('\n\ninter')
# print(peer_list)
# print(peer_num)
# print('inter\n\n')

for peer in sybil_peer:
    if peer_num[peer] <= 1:
        for i in range(2):
            peer_index = random.randint(0, len(sybil_peer) - 1)
            if peer_num[peers[peer_index]] < 4:
                flag = 0
                for i in peer_list.values():
                    if peers not in i:
                        pass
                    else:
                        flag = 1
                if flag is 0:
                    peer_list[peers[peer_index]].append(peer)
                    peer_num[peer] += 1
                    peer_num[peers[peer_index]] += 1

# print('\n')
print(peer_list)
print('\n')
print(peer_num)

