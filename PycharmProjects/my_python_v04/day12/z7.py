#!/usr/bin/env python3
#create host
import requests
import json
import pprint

url = 'http://192.168.4.11/api_jsonrpc.php'
headers = { 'Content-Type': 'application/json-rpc'}
data = {
    'jsonrpc': '2.0',
    'method': 'host.create',
    'params': {
        'host': 'mylinux',
        'interfaces': [
            {
                'type': 1,
                'main': 1,
                'useip': 1,
                'ip': '192.168.4.12',
                'dns': '',
                'port': '10050'
            }
        ],
        'groups': [
            {
                'groupid': '1'
            }
        ],
        'templates': [
            {
                'templateid': '10001'
            }
        ],
        'inventory_mode': 0,
        'auth': '76f5994bc6cc1da67c256fe2a7e5e2d0',
        'id': 3
    }
}


data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Linux server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.3.1",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "50"
            }
        ],
        "templates": [
            {
                "templateid": "20045"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "038e1d7b1735c6a5436ee9eae095879e",
    "id": 1
}

r = requests.post(url=url,headers=headers, data=json.dumps(data))
print(r.status_code)
