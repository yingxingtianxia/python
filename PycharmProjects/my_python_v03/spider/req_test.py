#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests
import time

login_url = 'http://ttsconsole.tmooc.cn/login'
index_url = 'http://ttsconsole.tmooc.cn/index'
data = {
    'loginName': 'lijiying',
    'pwd': 'lijiying1991',
}
headers = {
    'Host': 'ttsconsole.tmooc.cn',
    'User_Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}
s = requests.Session()
s.post(login_url, headers=headers, data=data)
time.sleep(3)
r = s.get(index_url)
print(r.text)