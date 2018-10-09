#!/usr/bin/env python3
#__*__coding: utf8__*__
from pyquery import PyQuery as pq

auth_list = []
for i in range(3):
    url = 'http://quotes.toscrape.com/page/%d/' % (i+1)
    doc = pq(url)
    divs = doc('div.quote')
    # print(len(divs))
    for div in divs:
        # print(pq(div)('small').text())
        # print(pq(div)('a').attr('href'))
        author = pq(div)('small').text()
        abstract = pq(div)('a').attr('href')
        auth_list.append(author)
        auth_list.append(abstract)

print(auth_list)
print(len(auth_list))