#!/usr/bin/env python3
import json
import requests
import pprint

##获取所有模板
#定义json返回函数
def reqjson(url, values):
    data = json.dumps(values)
    headers = {'Content-Type': 'application/json-rpc'}

    res = requests.post(url=url, headers=headers, data=data)
    output = res.json()

    return output
#定义获取auth函数
def get_auth(url, username, password):
    values = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params': {
            'user': username,
            'password': password
        },
        'id': 0
    }

    out = reqjson(url=url, values=values)
    authenticate = out['result']

    return authenticate
#定义获取template函数
def get_template(url,username,password):
    auth = get_auth(url,username, password)

    values = {
        'jsonrpc': '2.0',
        'method': 'template.get',
        'params': {
            'output': 'extend'
        },
        'auth': auth,
        'id': 1
    }

    out = reqjson(url=url,values=values)

    return out


if __name__ == '__main__':
    url = 'http://192.168.4.1/api_jsonrpc.php'
    username = 'admin'
    password = 'zabbix'

    out = get_template(url=url, username=username, password=password)
    tems = out['result']

    # print(type(tems))
    print(tems)
    print('模板id：模板名称')
    for tem in tems:
        t_id = tem['templateid']
        t_name = tem['name']

        print('[%s]: %s' % (t_id,t_name))
