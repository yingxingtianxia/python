#!/usr/bin/env python3
import requests

url = 'http://127.0.0.1/polls/2/vote/'
data = {'c_id': '7'}

for i in range(50):
    requests.post(url=url, data=data)