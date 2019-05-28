#!/usr/bin/env python3
import json
import requests
import pprint


##获取某个被监控主机的信息
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


#定义获取主机函数
#传参进去的主机名必须是被监控段端的真实主机名，不是可见主机名
def get_hosts(url,username,password,hostname):
    auth = get_auth(url, username,password)
    values = {
        'jsonrpc': '2.0',
        'method': 'host.get',
        'params': {
            'output': 'extend',
            'filter': {
                'host': [
                    hostname
                ]
            }
        },
        'auth': auth,
        'id': 1
    }

    out = reqjson(url,values)
    host_info = out['result'][0]

    return host_info
#host是主机的真是名称，对应创建主机页面的主机名称
#name是被监控主机的显示名称，对应创建主机页面的可见的名称



if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'
    hostname = 'zabbix_client_web1'

    host_info = get_hosts(url,username,password,hostname)
    # print(host_info)
    # pprint.pprint(host_info)
    id = host_info['hostid']
    host = host_info['host']
    available = host_info['available']


    cmds = {'0':'unknown', '1':'available', '2': 'unreachable'}

    print('被监控主机[%s]，id是[%s]，目前状态[%s]' % (host,id,cmds[available]))