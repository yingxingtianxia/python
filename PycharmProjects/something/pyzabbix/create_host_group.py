#!/usr/bin/env python3
import json
import requests

#创建群组
#定义获取json返回函数
def reqjson(url, values):
    data = json.dumps(values)
    headers = {'Content-Type': 'application/json-rpc'}

    res = requests.post(url=url, headers=headers, data=data)
    output = res.json()

    return output

#获取令牌
def get_auth(url, username, password):
    values = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params': {
            'user': username,
            'password':password
        },
        'id': '0'
    }

    out = reqjson(url=url, values=values)
    authenticate = out['result']

    return authenticate

#创建主机组
def create_host_group(url,username,password,groupname):
    auth = get_auth(url=url, username=username, password=password)

    values = {
        'jsonrpc': '2.0',
        'method': 'hostgroup.create',
        'params': {
            'name': groupname
        },
        'auth': auth,
        'id': 1
    }

    out = reqjson(url=url, values=values)
    group_id = out['result']['groupids']

    return group_id

if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'
    groupname = "My Servers"

    group_id = create_host_group(url=url, username=username, password=password, groupname=groupname)
    print(group_id)