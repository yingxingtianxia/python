#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests

# r = requests.get('http://www.baidu.com')
# print(r.text)
#
# r = requests.get('http://httpbin.org/get')
# print(type(r))
# obj = r.json()
# print(type(obj))
# print(obj)
#
# for key in obj.keys():
#     print(obj[key])

pyload = {
    'key1': 'value1',
    'key2': '["v1", "v2"]',
    'key3': 'value3',
}
r = requests.get('http://httpbin.org/get', params=pyload)
print(type(r))
print(r.text)
print(r.json())
# obj = r.json()
# for key in obj.keys():
#     if key == 'args':
#         for key in obj['args'].keys():
#             print(key, obj['args'][key])
#     else:
#         continue