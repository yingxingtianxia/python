#!/usr/bin/env python3
import requests
import json
import pprint

url = 'http://192.168.4.11/api_jsonrpc.php'
headers = { 'Content-Type': 'application/json-rpc' }

data = {
    'jsonrpc': '2.0',
    'method': 'host.get',
    'params': {
        'output': 'extend',
        'filter': {
            'host': [
                'Zabbix server',
                'Linux server'
            ]
        }
    },
    'auth': '8cc22085ff9573f6001e96e5110943c5',
    'id': 1
}

r = requests.post(url=url, headers=headers, data=json.dumps(data))
print(r)
pprint.pprint(r.json())