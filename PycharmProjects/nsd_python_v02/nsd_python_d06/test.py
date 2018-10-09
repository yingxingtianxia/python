#！/usr/bin/env python3
#--*--coding: utf8--*--
from urllib import request

keywd = 'hello'
url = "http://www.baidu.com/s?wd="+keywd
req = request.Request(url)
data = request.urlopen(req).read()

f = open('data.html', 'wb')
f.write(data)
f.close()