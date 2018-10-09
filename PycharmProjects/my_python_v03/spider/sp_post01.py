#!/usr/bin/env python3
#__*__coding: utf8__*__
import urllib.request
import urllib.parse

url = 'http://127.0.0.1:8888/login'

data = {'username':'admin', 'password':'admin'}
postdata = urllib.parse.urlencode(data).encode('utf8')
request = urllib.request.Request(url, data=postdata)
response = urllib.request.urlopen(request).read()

print(str(response, encoding='utf8'))