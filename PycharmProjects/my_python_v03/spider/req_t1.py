#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests
from pyquery import PyQuery as pq

url = 'http://www.baidu.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
#     'Host': 'www.baidu.com',
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
#}
r = requests.get(url)
# print(r.cookies.get_dict())
print(r)
print(type(r))
print(r.url)
# print(r.text)
# print(type(r.text))
# print(r.content)
# print(type(r.content))
# print(r.status_code)
#
# print(r.headers)
# print(type(r.headers))
#
# print(r.cookies)
# print(type(r.cookies))
#
# print(r.cookies.get_dict())


#
# doc = pq(url)
# print(doc)
# print(type(doc))
#
# print(doc('head'))