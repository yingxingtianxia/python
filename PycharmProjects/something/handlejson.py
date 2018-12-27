#!/usr/bin/env python3
import json

with open('dockerinfo.txt') as fobj:
    data = json.load(fobj)
    name = data['Name'].lstrip('/')
    ipaddr = data['NetworkSettings']['IPAddress']
    print('主机名是%s的容器的IP地址是：%s' % (name,ipaddr))
