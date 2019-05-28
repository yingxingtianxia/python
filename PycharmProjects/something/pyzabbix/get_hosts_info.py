#!/usr/bin/env python3
import json
import requests
import pprint

##获取多个被监控主机信息
#定义获取json返回函数
def reqjson(url,values):
    data = json.dumps(values)
    headers = {'Content-type': 'application/json-rpc'}

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

#定义获取多个主机函数
#传参进去的主机名必须是被监控段端的真实主机名，不是可见主机名
def get_hosts(url,username,password,hosts):
    auth = get_auth(url,username,password)

    values = {
        'jsonrpc': '2.0',
        'method': 'host.get',
        'params': {
            'output': 'extend',
            'filter': {
                'host': hosts
            }
        },
        'auth': auth,
        'id': 1
    }

    out = reqjson(url, values)
    hosts_info = out['result']


    return hosts_info




if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'
    hosts = ['zabbix_client_web1', 'zabbix server']

    hosts_info = get_hosts(url,username, password, hosts)
    # pprint.pprint(hosts_info)
    for host_info in hosts_info:
        id = host_info['hostid']
        host = host_info['host']
        available = host_info['available']

        cmds = {'0': 'unknown', '1': 'available', '2': 'unreachable'}

        print('被监控主机[%s]，id是[%s]，目前状态[%s]' % (host, id, cmds[available]))