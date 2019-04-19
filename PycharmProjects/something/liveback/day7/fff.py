#!/usr/bin/env python3
import requests
import pprint

url_get = 'http://www.weather.com.cn/data/zs/%s.html'

r = requests.get(url_get % ('101010400'))
r.encoding = 'utf-8'
data = r.json()

pprint.pprint(data)