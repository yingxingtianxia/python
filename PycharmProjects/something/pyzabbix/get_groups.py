#!/usr/bin/env python3
import json
import requests
import pprint

##获取所有群组
#定义获取json返回函数
def reqjson(url,values):
    data = json.dumps(values)
    headers = {'Content-Type': 'application/json-rpc'}

    res = requests.post(url=url,headers=headers, data=data)
    output = res.json()

    return output
#定义获取令牌函数
def get_auth(url,username,password):
    values = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params': {
            'user':username,
            'password':password
        },
        'id': 0
    }

    out = reqjson(url=url, values=values)
    authenticate = out['result']

    return authenticate
#定义获取主机组函数
def get_groups(url,username, password):
    auth = get_auth(url=url,username=username,password=password)
    values = {
        'jsonrpc': '2.0',
        'method': 'hostgroup.get',
        'params': {
            'output': 'extend'
        },
        'auth': auth,
        'id': 1
    }

    out = reqjson(url=url, values=values)

    return out


if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'
    out = get_groups(url=url, username=username, password=password)
    groups = out['result']
    # print(type(groups))
    pprint.pprint(groups)
    print("群组id：群组名")
    for group in groups:
        g_id = group['groupid']
        g_name = group['name']

        print('[%s]: %s' % (g_id,g_name))