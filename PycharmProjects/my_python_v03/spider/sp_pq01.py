#!/usr/bin/env python3
#__*__coding: utf8__*__
from pyquery import PyQuery as pq

doc = pq('http://127.0.0.1:8000/blog/show')
trs = doc('tr[id]')
for tr in trs:
    title = pq(tr)('td:eq(0)').text()
    desc = pq(tr)('td:eq(1)').text()
    print(title, desc)
print(len(trs))