#!/usr/bin/env python3
#__*__coding: utf8__*__
import urllib.request

proxy = urllib.request.ProxyHandler({'http': '140.143.105.229:80'})
opener = urllib.request.build_opener(proxy)
#opener.addheaders = [('User-Agent:','Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0')]
urllib.request.install_opener(opener)

page = opener.open('http://2018.ip138.com/ic.asp').read()
page = page.decode('gb18030')
print(page)