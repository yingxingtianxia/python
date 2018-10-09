#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests

url = 'http://127.0.0.1:8000/blog/del'
pyload = {'id': 109}
headers = {'Cookie':"csrftoken=kVYo8fKnCBbfGb4nWKtaJjFlN6fj3mUX; sessionid=dcn0up6ms6laahbpn1i10fe9l1qi7w9u; uid=2|1:0|10:1537346228|3:uid|0:|4818e31a4dc301b16702be5730b3d7ae657f5d2d7c2d24719fa4fb7419cdddfe"}
r = requests.post(url, data=pyload, headers=headers)
print(r.text)