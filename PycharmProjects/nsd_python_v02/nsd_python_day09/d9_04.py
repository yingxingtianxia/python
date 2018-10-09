#!/usr/bin/env python
#--coding: utf8--
import urllib2

html = urllib2.urlopen('http://www.baidu.com/')
data = html.read()
html.close()

with open('index.html', 'w') as f:
    f.write(data)