#!/usr/bin/env python3
#__*__coding: utf8__*__
from pyquery import PyQuery as pq

doc = pq('http://127.0.0.1:8000/blog/show')
trs = doc('table > tr')

for tr in trs[1:]:
    title = pq(tr)('td:eq(0)').text()
    print(title)