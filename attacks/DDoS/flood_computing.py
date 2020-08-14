# -*- coding: utf-8 -*-
"""
    webchain
    ~~~~~~~~

    A http server for computation flood

    :author: Yinqiu Liu
"""

from flask import Flask, request, jsonify
import struct
import socket
import hashlib
import requests
from random import randrange, seed
from binascii import unhexlify

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
import time
from io import BytesIO

app = Flask(__name__)

f = BytesIO()
@app.route("/test", methods=['GET', 'POST'])
def memory():
    for i in range(1, 30000):
        f.write('everything')
        f.write('is')
        f.write('possibile')
    return 'ok'
    

@app.route("/flood", methods=['GET', 'POST'])
def computing():
    ti = time.time()
    initial = randrange(0, 2 ** 10)
    for nonce in range(initial, 2 ** 20):
        sha = hashlib.sha256()
        sha.update(b'\x0000000\x03\x34\x5f0000defsfaefefee')
        sha.update(struct.pack('=I', nonce))
        hash_ = sha.digest()
        sha = hashlib.sha256()
        sha.update(hash_)
        hash_ = sha.digest()
        if hash_ is b'a31':
            break
    
    return str(time.time() - ti)


if __name__ == "__main__":
    app.run()
