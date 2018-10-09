#!/usr/bin/env python3
# -*-coding: utf8-*-
h = input('h:')
m = input('m:')
s = input('s:')
#print('time is ' + h + ':' + m + ':' + s)
hs = int(int(h) * 3600)
ms = int(int(m) * 60)
ss = int(s)
print(hs + ms + ss)
