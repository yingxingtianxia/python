#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests

url = 'http://2018.ip138.com/ic.asp'
proxies = {
    'https': 'https://151.106.12.245:1080',
    'http': 'http:/50.226.134.50:80/',
    'http': 'http://111.7.130.101:8080',
}

r = requests.get(url, proxies=proxies)
print(r.text)