#!/usr/bin/env python3
import requests
import json

##获取zabbix登陆令牌
#定义获取json返回函数
def reqjson(url, values):
    data = json.dumps(values)
    headers = {'Content-Type': 'application/json-rpc'}

    res = requests.post(url=url, headers=headers, data=data)
    output = res.json()

    return output

#传参
def get_auth(url,username,password):
    values = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params':{
            'user': username,
            'password': password
        },
        'id': 1
    }

    output = reqjson(url=url, values=values)

    return output

if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'

    out = get_auth(url=url, username=username, password=password)
    authenticate = out['result']
    print(authenticate)