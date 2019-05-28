#!/usr/bin/env python3
import json
import requests
import sys
import pprint

##获取某个主机群组内的所有主机
#定义获取json返回函数
def reqjson(url,values):
    data = json.dumps(values)
    headers = {'Content-Type': 'application/json-rpc'}
    res = requests.post(url=url,headers=headers,data=data)
    output = res.json()

    return output

#定义获取令牌函数
def get_auth(url,username,password):
    values = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params': {
            'user': username,
            'password': password
        },
        'id': 0
    }

    out = reqjson(url,values)
    authenticate = out['result']

    return authenticate
#定义获取所有主机组函数
def get_groups(url,username,password):
    auth = get_auth(url,username,password)
    values = {
        'jsonrpc': '2.0',
        'method': 'hostgroup.get',
        'params': {
            'output': 'extend'
        },
        'auth': auth,
        'id': 1
    }
    out = reqjson(url,values)
    groups = out['result']

    groups_dict = {}
    for group in groups:
        g_name = group['name']
        g_id = group['groupid']
        groups_dict[g_name] = g_id

    return groups_dict
#定义获取组内所有主机函数
def get_group_hosts(url,username,password,groupname):
    auth = get_auth(url,username,password)
    groups_dict = get_groups(url,username,password)
    if groupname not in groups_dict.keys():
        print('群组不存在，请退出检查')
        sys.exit(1)
    group_id = groups_dict[groupname]

    values = {
        'jsonrpc': '2.0',
        'method': 'host.get',
        'params': {
            'output': 'extend',
            'groupids': group_id
        },
        'auth': auth,
        'id': 3
    }

    out = reqjson(url,values)
    hosts = out['result']

    return hosts

if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'
    groupname = 'My Servers'

    hosts = get_group_hosts(url,username,password,groupname)
    print(hosts)