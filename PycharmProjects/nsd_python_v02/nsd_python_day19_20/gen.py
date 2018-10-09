#!/usr/bin/env python3
#--*--coding: utf8--*--
from urllib.request import urlopen
from urllib import error
from random import randint





mac = ['32:00:04:5a:34:20', '32:00:04:5a:34:21',
       '32:00:04:5a:34:22', '32:00:04:5a:34:23',
       '32:00:04:5a:34:24', '32:00:04:5a:34:25']
device = ['iphone', 'sumsung', 'skyworthTV', 'xiaomiTV', 'HTC3001']
app = ['kuwoMobilePLayer', 'kuwoTVKtv', 'kuwoPcPlayer', 'kuwoTvRadio', 'kuwoMobileKTV']
ver = ['2.0.1', '5.5.6', '2.1.4', '10.4.5', '6.1.13']
content = ['song103', 'song213', 'song301', 'song302', 'song234', 'song478']
act = ['play', 'save', 'download', 'like', 'share']

def getuser():
    return 'u%03d' % randint(1, 299)

def getany(list):
    return '%s' % list[randint(0, len(list)-1)]

def getinfo():
    info = '%s/%s/%s/%s/%s/%s/%s' % (getuser(), getany(mac),
                                     getany(device), getany(app),
                                     getany(ver), getany(act), getany(content))
    return info

def get_gen(url, counts):
    for i in range(counts):
        try:
            urlopen(url+getinfo())
        except error.HTTPError:
            continue

if __name__ == '__main__':
    url = 'http://127.0.0.1/loggen/'
    get_gen(url, 300)