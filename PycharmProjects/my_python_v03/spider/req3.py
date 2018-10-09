#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests

url = 'http://www.goubanjia.com'
header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Referer': 'http://www.baidu.com',
}
r = requests.get(url, headers=header)
print(r.text)