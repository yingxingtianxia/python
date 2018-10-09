#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests

pyload = {
    'username': 'admin',
    'password': 'admin',
}

r = requests.post('http://127.0.0.1:8888/login', params=pyload)
print(r.text)