#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests
import time

url = 'http://127.0.0.1:8888/login'
data = {
    'username': 'admin',
    'password': 'admin',
}

s = requests.Session()
s.post(url, data=data)
print(s)
time.sleep(3)
r = s.get('http://127.0.0.1:8888')
print(r.text)