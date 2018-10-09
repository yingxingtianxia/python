#!/usr/bin/env python3
#__*__coding: utf8__*__
import urllib.request

response = urllib.request.urlopen('http://python.org')
html = response.read()
print(html)