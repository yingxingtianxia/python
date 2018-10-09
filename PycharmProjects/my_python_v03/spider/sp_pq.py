#!/usr/bin/env python3
#__*__coding: utf8__*__
from pyquery import PyQuery as pq

# doc = pq('<html><a>abc</a></html>')
# print(doc.html())
# print(doc.text())

doc = pq('http://127.0.0.1:8000/blog/show')
# print(type(doc))
# print(doc.html())
print(doc.text())