#!/usr/bin/env python3
import json
import requests
import sys

##添加主机
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

    out = reqjson(url=url,values=values)
    authenticate = out['result']

    return authenticate
#定义获取主机群组函数
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

    out = reqjson(url, values)
    groups = out['result']
    groups_dict = {}

    for group in groups:
        g_id = group['groupid']
        g_name = group['name']

        groups_dict[g_name] = g_id

    return groups_dict

#定义获取监控模板函数
def get_tems(url,username,password):
    auth = get_auth(url, username, password)
    values = {
        'jsonrpc': '2.0',
        'method': 'template.get',
        'params': {
            'output': 'extend'
        },
        'auth': auth,
        'id': 2
    }

    out = reqjson(url, values)
    tems = out['result']
    templates_dict = {}

    for tem in tems:
        t_id = tem['templateid']
        t_name = tem['name']
        templates_dict[t_name] = t_id

    return templates_dict

#定义创建主机函数
def create_host(url,username,password,hostname,ipaddr,group,template):
    auth = get_auth(url,username,password)

    groups_dict = get_groups(url,username,password)
    if group not in groups_dict.keys():
        print('群组不存在，请退出检查')
        sys.exit(1)
    g_id = groups_dict[group]

    templates_dict = get_tems(url,username,password)
    if template not in templates_dict.keys():
        print('模板不存在，请退出检查')
        sys.exit(1)
    t_id = templates_dict[template]

    values = {
        'jsonrpc': '2.0',
        'method': 'host.create',
        'params': {
            'host': hostname,
            'interfaces': [
                {
                    'type': 1,
                    'main': 1,
                    'useip': 1,
                    'ip': ipaddr,
                    'dns': '',
                    'port': '10050'
                }
            ],
            'groups': [
                {
                    'groupid': g_id
                }
            ],
            'templates': [
                {
                    'templateid': t_id
                }
            ],
            'inventory_mode': 0,
        },
        'auth': auth,
        'id': 3
    }

    out = reqjson(url=url, values=values)
    print(out)
    host_id = out['result']['hostids'][0]

    return host_id

if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'
    hostname = 'zabbix_client_web1'
    ipaddr = '192.168.4.2'
    group = 'My Servers'
    template = 'Template OS Linux'
    # g_d = get_groups(url,username,password)
    # print(g_d)
    # t_d = get_tems(url,username,password)
    # print(t_d)

    h_id = create_host(url,username,password,hostname,ipaddr,group,template)
    print(h_id)