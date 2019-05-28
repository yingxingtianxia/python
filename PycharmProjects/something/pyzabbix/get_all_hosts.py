#!/usr/bin/env python3
import json
import requests
import sys
import pprint

##获取当前所有被监控的主机
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

#定义获取所有群组函数
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

#定义获取所有主机函数
def get_all_hosts(url,username,password):
    auth = get_auth(url,username,password)
    g_dict = get_groups(url,username,password)
    group_host_dict = {}
    for g_name in g_dict.keys():
        g_id = g_dict[g_name]
        values = {
            'jsonrpc': '2.0',
            'method': 'host.get',
            'params': {
                'output': 'extend',
                'groupids': g_id
            },
            'auth': auth,
            'id': 3
        }
        out = reqjson(url,values)
        hosts = out['result']

        group_host_dict[g_name] = hosts

    return group_host_dict

if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'

    all_hosts = get_all_hosts(url,username,password)

    for i in all_hosts.keys():
        if all_hosts[i] == []:
            print('群组[%s]内没有被监控主机' % (i))
        else:
            cmds = {'0': '未知','1':'可用','2': '不可用'}
            all_hosts_info = all_hosts[i]
            hn = len(all_hosts_info)
            print('群组[%s]内有%s个被监控主机' % (i, hn))
            for info in all_hosts_info:
                h_id = info['hostid']
                h_name = info['host']
                h_sta = cmds[info['available']]
                print('该组内名为%s的主机组内编号是%s，当前状态%s' % (h_name,h_id,h_sta))
