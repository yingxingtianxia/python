#!/usr/bin/env python3
import requests

# payload = {'wd': 'centos7'}
#
# r = requests.get(url='http://www.baidu.com/s', params=payload)
# print(r)
#################################################
# header = {
#     'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
# }
# header = {
#     'User-Agent': 'woshinidaye'
# }
# r = requests.get(url='http://127.0.0.1/', headers=header)
######################################################

r = requests.get(url='http://www.baidu.com')
