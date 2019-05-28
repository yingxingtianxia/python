#!/usr/bin/env python3
import requests
import json

##获取zabbix版本信息
#定义获取json返回格式函数
def reqjson(url, values):
    data = json.dumps(values)

    headers = {'Content-Type': 'application/json-rpc'}

    res = requests.post(url=url, headers=headers, data=data)

    output = res.json()

    return output

#传参
def get_ver(url, username, password):
    values = {
        'jsonrpc': '2.0',
        'method': 'apiinfo.version',
        'params':[],
        'id': 0
    }

    output = reqjson(url=url, values=values)

    return output


if __name__ == '__main__':
    url = "http://192.168.4.1/api_jsonrpc.php"
    username = 'admin'
    password = 'zabbix'

    out = get_ver(url, username, password)
    print(out)