#!/usr/bin/env python3
#--*--coding: utf8--*--
import urllib.request

file = urllib.request.urlopen('http://www.baidu.com')
data = file.read()
#dataline = file.readline()
fhandle = open("index.html", 'wb')
fhandle.write(data)
fhandle.close()