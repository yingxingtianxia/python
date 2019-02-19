#!/usr/bin/env python3
import requests
import json

url = 'http://192.168.4.11/api_jsonrpc.php'
headers = {
    'Content-Type': 'application/json-rpc'
}

data = {
    'jsonrpc': '2.0',
    'method': 'user.login',
    'id': 1,
    'params': {
        'user': 'admin',
        'password': 'zabbix'
    }
}

r = requests.post(url=url, headers=headers, data=json.dumps(data))
print(r.json())