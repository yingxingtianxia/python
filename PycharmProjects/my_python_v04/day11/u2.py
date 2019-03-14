#!/usr/bin/env python3
from urllib import request

url = 'http://127.0.0.1/'
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

r = request.Request(url, headers=header)
html = request.urlopen(r)

data = html.read()
print(data.decode('utf8'))