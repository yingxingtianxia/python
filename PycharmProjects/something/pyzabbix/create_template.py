#!/usr/bin/env python3
import json
import requests
import sys

##创建模板与主机组相关，模板必须与主机组相关联，页面上可以在创建模板的同时创建主机组
##api接口里边必须先创建主机组，因为groups是创建模板的必要参数

##页面上可以在把模板-应用集-监控项-触发器-图形都配置后以后再链接到主机
##api接口里边可以在创建模板的同时就把模板链接到主机

#定义获取json返回格式函数
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

    out = reqjson(url, values)
    authenticate = out['result']

    return authenticate

#定义获取所有主机组函数
def get_groups(url,username,password):
    auth = get_auth(url,username, password)
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
def get_hosts(url,username,password, groupname):
    auth = get_auth(url,username,password)
    groups_dict = get_groups(url,username,password)
    if groupname not in groups_dict.keys():
        print('主机群组不存在，请退出检查')
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
        'id': 2
    }

    out = reqjson(url,values)
    hosts = out['result']
    group_hosts_dict = {}
    group_hosts_dict['group_id'] = group_id
    hostids_list = []
    for host in hosts:
        h_dict = {}
        id = host['hostid']
        h_dict['hostid'] = id
        hostids_list.append(h_dict)
    group_hosts_dict['group_hosts'] = hostids_list

    return group_hosts_dict

#定义创建模板函数
def create_template(url,username,password,groupname,templatename):
    auth = get_auth(url,username,password)
    gh_dict = get_hosts(url,username,password,groupname)
    g_id = gh_dict['group_id']
    g_hosts = gh_dict['group_hosts']
    values = {
        'jsonrpc': '2.0',
        'method': 'template.create',
        'params': {
            'host': templatename,
            'groups': {
                'groupid': g_id
            },
            'hosts': g_hosts,
        },
        'auth': auth,
        'id': 3
    }

    out = reqjson(url,values)
    tem_info = out['result']

    return tem_info

if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'
    hostgroup = 'My Servers'
    templatename = 'My Templates'

    tem_info = create_template(url,username,password,hostgroup,templatename)
    print(tem_info)