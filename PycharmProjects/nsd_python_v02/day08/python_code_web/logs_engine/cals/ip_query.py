#!/usr/bin/python
# coding=utf-8

from urllib import urlopen
import json

ips = ['120.25.63.167', '58.21.1.2', '58.207.96.2', '59.76.192.3']

for ip in ips:
    url = "http://ip.taobao.com/service/getIpInfo.php?ip=" + str(ip)
    loc = urlopen(url).read()
    s = json.loads(loc)
    print s['data']['city'], s['data']['region']
