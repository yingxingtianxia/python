#!/usr/bin/env python
#--coding: utf8--
import urllib2

html = urllib2.urlopen('http://192.168.4.254/sky.jpg')
data = html.read()
html.close()

with open('a.jpg', 'w') as fobj:
    fobj.write(data)