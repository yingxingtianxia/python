#!/usr/bin/env python3
import requests
import json
import pprint

url = 'http://192.168.4.11/api_jsonrpc.php'
headers = { 'Content-Type': 'application/json-rpc' }

data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectGroups": "extend",
        "filter": {
            "host": [
                "Zabbix server"
            ]
        }
    },
    "auth": "f8de9888ad97bbb43620662f4ea72d9e",
    "id": 2
}

r = requests.post(url=url,headers=headers, data=json.dumps(data))
print(r.status_code)
pprint.pprint(r.json())