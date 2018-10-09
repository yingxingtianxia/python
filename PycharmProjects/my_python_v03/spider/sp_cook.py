#!/usr/bin/env python3
#__*__coding: utf8__*__
import http.cookiejar
import urllib.request
import urllib.parse

cj = http.cookiejar.CookieJar()
openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
data = {'username':'admin', 'password':'admin'}
r = openner.open(
    "http://127.0.0.1:8888/login",
    data=urllib.parse.urlencode(data).encode('utf8')
                 )
print(r.read())
r = openner.open('http://127.0.0.1:8888')
print(r.read())